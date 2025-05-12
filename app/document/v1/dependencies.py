from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer

from app.config import settings
from app.core.auth import auth_core
from app.helper.error_helper import errors
from app.helper.redis_helper import session_helper
from app.helper.secret_helper import secret_helper
from app.models.enums import Status
from app.models.user import User


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/document" + settings.API_VERSION_STR + "/auth/token/email"
)


def get_current_user(
    request: Request,
    token: str = Depends(reusable_oauth2),
):
    with session_helper:
        session, exp_time = session_helper.get_session(token)

        if session is None or session != settings.USER_SESSION_STATUS:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=errors.invalid_access_session,
            )

        if session == settings.USER_DISABLED_SESSION_STATUS:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=errors.disabled_session
            )

        if session == settings.USER_BLOCKED_SESSION_STATUS:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=errors.invalid_access_token,
            )

        token_data = secret_helper.verify_token(token)
        db = request.state.db
        user = auth_core.get_user_by_email(
            db, email=token_data["email"], only_active=False
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=errors.user_not_found
            )

        session_helper.set_session(token, user_id=user.id)

    request.state.access_token = token
    return user


def get_current_active_user(
    request: Request, current_user: User = Depends(get_current_user)
):
    if current_user.status != Status.active:
        with session_helper:
            session_helper.set_session(
                request.state.access_token,
                user_id=current_user.id,
                value=settings.USER_BLOCKED_SESSION_STATUS,
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=errors.deactivate_user
            )

    return current_user
