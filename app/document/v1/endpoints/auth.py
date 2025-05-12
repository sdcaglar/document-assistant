from fastapi import APIRouter
from fastapi import HTTPException, Request, status
from app.helper.error_helper import errors

from app.core.auth import auth_core


from app.document.v1.schemas import MessageOut
from app.document.v1.schemas.auth import RegisterIn, LoginIn, LoginOut
from app.helper.hash_helper import hash_helper
from app.models.enums import Status

router = APIRouter()


@router.post("/register", response_model=MessageOut, summary="Create User")
def register(request: Request, register_schema: RegisterIn):
    db = request.state.db
    user = auth_core.get_user_by_email(db, email=register_schema.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=errors.email_already_exists
        )

    return auth_core.create_user(
        db,
        register_schema.first_name,
        register_schema.last_name,
        register_schema.email,
        register_schema.password,
    )


@router.post("/login", response_model=LoginOut, summary="Login User")
def login(request: Request, login_schema: LoginIn):
    db = request.state.db
    user = auth_core.get_user_by_email(db, email=login_schema.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=errors.user_not_found
        )

    if user.status != Status.active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=errors.deactivate_user
        )

    if not hash_helper.verify(user.password_hash, login_schema.password):
        # TODO: add login record (fail)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=errors.invalid_login
        )

    return auth_core.login_user(user)
