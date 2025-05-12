import time
from datetime import datetime, timedelta

import redis

from app.config import settings

redis_connection_pool = redis.ConnectionPool.from_url(settings.REDIS_URI)


class RedisHelper:
    def __init__(self):
        self.expire_time = settings.JWT_EXPIRES_TIME
        self.user_session_status = settings.USER_SESSION_STATUS

    def check_redis_health(self, max_retries=3, interval=1):
        try:
            # Attempt to create a Redis connection and immediately close it
            with redis.StrictRedis(
                connection_pool=redis_connection_pool
            ).pipeline() as pipe:
                pipe.ping()
                pipe.execute()
            return True  # If successful, consider Redis healthy
        except redis.RedisError:
            # Log the error and wait for the specified interval
            time.sleep(max_retries * interval)

        return False  # Redis health check failed.

    def _connection(self):
        return redis.Redis(connection_pool=redis_connection_pool)

    def get(self, key):
        return self.conn.get(key)

    def set(self, key, value):  # noqa: A003
        self.conn.set(key, value)

    def expire(self, key, expire=None):
        self.conn.expire(key, expire or self.expire_time)

    def delete(self, key):
        self.conn.delete(key)

    def __enter__(self):
        self.conn = self._connection()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()


class PanelSessionHelper(RedisHelper):
    def get_session(self, key):
        return self.get(key)

    def set_session(self, key):
        self.set(key, self.user_session_status)
        self.expire(key)

    def delete_session(self, key):
        return self.delete(key)


class WalletSessionHelper(RedisHelper):
    def _parse_value_and_expire(self, value):
        if not value:
            return None, None
        v = None
        t = None
        try:
            if isinstance(value, bytes):
                value = value.decode("utf8")
            values = value.split("|")
            v = values[0]
            t = datetime.fromisoformat(values[1])
        except:  # noqa
            pass

        return v, t

    def get_session(self, key, only_expired_keys=False):
        value = self.conn.get(key)
        v, t = self._parse_value_and_expire(value)
        if not v or not t:
            return None, None

        now = datetime.now() - timedelta(seconds=self.expire_time)

        check = t > now if only_expired_keys else t < now

        if check:
            return None, None

        return v, t

    def set_session(self, key, value=None):
        self.conn.set(
            key, f"{value or self.user_session_status}|{datetime.now().isoformat()}"
        )

    def update_if_exist(self, key, value=None, update_expire=True):
        val = self.conn.get(key)
        v, t = self._parse_value_and_expire(val)

        if not v:
            return
        if update_expire:
            t = datetime.now()

        self.conn.set(
            key,
            f"{value or v}|{t.isoformat() if isinstance(t, datetime) else (t or '')}",
        )


redis_helper = RedisHelper()
