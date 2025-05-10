import os

from pydantic import BaseSettings

from app.helper.version_helper import get_release_no, get_version


class DefaultSettings(BaseSettings):
    API_VERSION_STR: str = "/v1"

    BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    APP_VERSION: str = get_version(BASEDIR)
    RELEASE_NO: str = get_release_no(BASEDIR)
    PROJECT_NAME: str = "Document Assistant"

    # POSTGRESQL
    USER = os.getenv("POSTGRESQL_USER", "root")
    PASSWD = os.getenv("POSTGRESQL_ROOT_PASSWORD", "rootpasswd")
    HOST = os.getenv("POSTGRESQLL_HOST", "127.0.0.1")
    PORT = os.getenv("POSTGRESQL_PORT", "3306")
    DB = os.getenv("POSTGRESQL_DATABASE", "myth-db")
    SQLALCHEMY_DB_URI: str = f"mysql://{USER}:{PASSWD}@{HOST}:{PORT}/{DB}?charset=utf8"

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

    # OTHER
    TIMEZONE = "Europe/Istanbul"
    DEVELOPER_MODE = True
