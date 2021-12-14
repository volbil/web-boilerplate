from .models import User

class UserService(object):
    @classmethod
    def get_by_username(cls, username):
        return User.get(username=username)

    @classmethod
    def get_by_email(cls, email):
        return User.get(email=email)

    @classmethod
    def create(cls, username, email, password):
        return User(
            username=username, password=password,
            email=email
        )
