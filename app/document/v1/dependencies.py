from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.auth import auth_core
from app.db.database import get_db
from app.helper.error_helper import ErrorCode as errors
from app.helper.secret_helper import secret_helper
from app.models.enums import Status
from app.models.user import User

reusable_oauth2 = HTTPBearer()


def get_user_by_token(
    db: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(reusable_oauth2),
):
    token_data = secret_helper.verify_token(token.credentials)
    user = auth_core.get_user_by_email(db, email=token_data["email"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=errors.user_not_found
        )

    return user


def get_current_active_user(
    user: User = Depends(get_user_by_token),
):
    if user.status != Status.active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=errors.deactivate_user
        )
    return user
