from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

# engine = create_engine(settings.SQLALCHEMY_DB_URI, connect_args={})
engine = create_engine(
    settings.SQLALCHEMY_DB_URI, connect_args={"options": "-c client_encoding=utf8"}
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def init_db() -> None:
    Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
