from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashHelper:
    def __init__(self):
        pass

    def get_password_hash(self, password):
        return pwd_cxt.hash(password)

    def verify(self, hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)


hash_helper = HashHelper()
