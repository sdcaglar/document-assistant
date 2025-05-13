import os
from typing import Any

from pydantic_settings import BaseSettings

from app.helper.version_helper import get_release_no, get_version


class DefaultSettings(BaseSettings):
    API_VERSION_STR: str = "/v1"
    BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    APP_VERSION: str = get_version(BASEDIR)
    RELEASE_NO: str = get_release_no(BASEDIR)
    PROJECT_NAME: str = "Document Assistant"

    # POSTGRESQL
    USER = os.getenv("POSTGRESQL_USER", "postgres")
    PASSWD = os.getenv("POSTGRESQL_ROOT_PASSWORD", "rootpasswd")
    HOST = os.getenv("POSTGRESQLL_HOST", "127.0.0.1")
    PORT = os.getenv("POSTGRESQL_PORT", "5432")
    DB = os.getenv("POSTGRESQL_DATABASE", "myth-db")
    SQLALCHEMY_DB_URI: str = f"postgresql+psycopg2://{USER}:{PASSWD}@{HOST}:{PORT}/{DB}"

    # SQLALCHEMY SETTINGS
    SQLALCHEMY_CONNECT_ARGS: dict = {"charset": "utf8mb4", "connect_timeout": 10}
    SQLALCHEMY_MAX_OVERFLOW: int = 12
    SQLALCHEMY_POOL_RECYCLE: int = 1800
    SQLALCHEMY_POOL_SIZE: int = 6
    SQLALCHEMY_POOL_TIMEOUT: int = 10

    # JWT
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRES_TIME = 10000
    SECRET_KEY: str = "secret_key"

    # REDIS
    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"
    REDIS_PASSWORD: Any = os.getenv("REDIS_PASSWORD", "")
    REDIS_DB = "0"
    REDIS_URI = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

    # MONGODB
    MONGODB_HOST = "localhost"
    MONGODB_PORT = "27017"
    MONGODB_URI: str = f"mongodb://{MONGODB_HOST}:{MONGODB_PORT}"
    MONGODB_DB_NAME: str = "myth-db"
    MONGODB_CONNECT_TIMEOUT_MS: int = 10000
    MONGODB_SERVER_SELECTION_TIMEOUT_MS: int = 5000
    MONGODB_SOCKET_TIMEOUT_MS: int = 10000
    MONGODB_MAX_POOL_SIZE: int = 10
    MONGODB_MIN_POOL_SIZE: int = 1

    # GEMINI
    GEMINI_API_KEY: str = "AIzaSyDiQ4bUan99BjoG-1ckIlCC2OmgZBZkGV0s"
    GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/openai/"

    # OTHER
    TIMEZONE = "Europe/Istanbul"
    DEVELOPER_MODE = True
    USER_SESSION_STATUS = "access"
    USER_DISABLED_SESSION_STATUS = "disabled"
    USER_BLOCKED_SESSION_STATUS = "blocked"

    model_config = {"ignored_types": (str, int)}
