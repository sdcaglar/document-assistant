from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import column_property

from app.models.base import ModelBase
from app.models.enums import Status


class User(ModelBase):
    __tablename__ = "user"

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    full_name = column_property(first_name + " " + last_name)
    email = Column(String(50), nullable=False)
    password_hash = Column(String(120), nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.active)
