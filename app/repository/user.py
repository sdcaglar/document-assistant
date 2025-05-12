from app.models.enums import Status
from app.models.user import User


class UserRepository:
    def __init__(self):
        pass

    def get_user_by_email(self, db, email: str, only_active=True):
        filter_arry = [User.email == email, User.status != Status.deleted]
        if only_active:
            filter_arry.append(User.status == User.active)

        return db.query(User).filter(*filter_arry).first()

    def create_user_object(self, db, **kwargs):
        user = User(**kwargs)
        db.add(user)
        db.commit()
        return user


user_repository = UserRepository()
