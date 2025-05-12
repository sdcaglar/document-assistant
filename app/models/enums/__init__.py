from app.models.enums.base import BaseEnum


class Status(int, BaseEnum):
    active = 1
    passive = 0
    deleted = -1
