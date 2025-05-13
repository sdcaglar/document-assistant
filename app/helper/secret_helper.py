import uuid
from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import HTTPException, status

from app.config import settings
from app.helper.error_helper import errors


class SecretHelper:
    def __init__(self):
        pass

    @staticmethod
    def create_access_token(
        data: dict,
        expires_delta: Optional[timedelta] = None,
    ):
        to_jwt_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(seconds=settings.JWT_EXPIRES_TIME)

        to_jwt_encode.update({"exp": expire, "_t": str(uuid.uuid4())})
        return jwt.encode(
            to_jwt_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        ), expire

    @staticmethod
    def verify_token(token: str):
        try:
            data = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
            )
            if data is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=errors.invalid_access_token,
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return data
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=errors.invalid_access_token,
                headers={"WWW-Authenticate": "Bearer"},
            )


secret_helper = SecretHelper()
