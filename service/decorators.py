from .services import UserService
from datetime import datetime
from functools import wraps
from flask import request
from .token import Token
from .abort import abort

def auth_required(view_function):
    @wraps(view_function)
    def decorator(*args, **kwargs):
        token = request.headers.get("Authentication")

        valid = Token.validate(token)
        payload = Token.payload(token)

        if valid and payload["action"] == "login":
            account = UserService.get_by_username(payload["meta"])

            if account is None:
                return abort("account", "login-failed")

            account.login = datetime.utcnow()
            request.account = account

            return view_function(*args, **kwargs)

        return abort("account", "login-failed")

    return decorator
