from app.helper.hash_helper import hash_helper
from app.helper.secret_helper import secret_helper
from app.models.enums import Status
from app.repository.user import user_repository


class AuthCore:
    def __init__(self):
        pass

    def create_user(self, db, first_name, last_name, email, password):
        user_repository.create_user_object(
            db,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=hash_helper.get_password_hash(password),
            status=Status.active,
        )
        return {"message": "User registered successfully"}

    def get_user_by_email(self, db, email: str, only_active: bool = False):
        return user_repository.get_user_by_email(db, email, only_active)

    def login_user(self, user, email):
        access_token, expire = secret_helper.create_access_token(
            {"fullname": user.full_name, "email": email}
        )
        return {"access_token": access_token, "token_type": "bearer"}


auth_core = AuthCore()
