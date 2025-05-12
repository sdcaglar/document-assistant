import re
from gettext import gettext as _
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class RegisterIn(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: str
    password: str = Field(min_length=6, max_length=6)

    @field_validator("email")
    def validate_email(cls, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            raise ValueError("Geçersiz e-posta adresi")
        return email

    @field_validator("password")
    def check_password(cls, v):
        if not v.isdecimal():
            raise ValueError(_("Şifreniz rakamlardan oluşmalı"))
        return v


class LoginIn(BaseModel):
    email: str
    password: str = Field(min_length=6, max_length=6)

    @field_validator("email")
    def validate_email(cls, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            raise ValueError("Geçersiz e-posta adresi")
        return email

    @field_validator("password")
    def check_password(cls, v):
        if not v.isdecimal():
            raise ValueError(_("Şifreniz rakamlardan oluşmalı"))
        return v


class LoginOut(BaseModel):
    access_token: Optional[str] = None
    token_type: Optional[str] = None
