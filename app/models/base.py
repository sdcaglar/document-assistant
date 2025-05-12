from datetime import datetime

from pytz import timezone
from sqlalchemy import Column
from sqlalchemy import DateTime as SdateTime
from sqlalchemy import Integer
from sqlalchemy.types import TypeDecorator

from app.config import settings
from app.db.database import Base


class DateTime(TypeDecorator):
    impl = SdateTime
    cache_ok = True

    def process_bind_param(self, value, engine):
        if value:
            return value
        return datetime.now(timezone(settings.TIMEZONE))

    def process_result_value(self, value, engine):
        return value


class ModelBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, default=datetime.now)
    date_modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
