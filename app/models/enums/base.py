from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def __get_validators__(cls):
        cls.lookup = {v: k.value for v, k in cls.__members__.items()}
        cls.keys = [*cls.lookup]
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="str", enum=cls.keys)

    @classmethod
    def validate(cls, v):
        if isinstance(v, Enum):
            return v
        try:
            _ = cls.lookup[v]
            return cls[v]
        except KeyError:
            permitted = ", ".join(v for v in cls.keys)
            raise ValueError(
                f"value is not a valid enumeration member; permitted: {permitted}"
            )
