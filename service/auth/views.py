from webargs.flaskparser import use_args
from .args import join_args, login_args
from ..services import UserService
from datetime import datetime
from flask import Blueprint
from ..token import Token
from ..abort import abort
from pony import orm
from .. import utils

blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@blueprint.route("/join", methods=["POST"])
@use_args(join_args, location="json")
@orm.db_session
def join(args):
    result = {"error": None, "data": {}}

    username = args["username"]
    email = args["email"]

    if UserService.get_by_username(username):
        return abort("account", "username-exist")

    if UserService.get_by_email(email):
        return abort("account", "email-exist")

    password = utils.hashpwd(args["password"])
    account = UserService.create(
        args["username"], args["email"], password
    )

    result["data"] = {
        "login": int(datetime.timestamp(account.login)),
        "username": account.username
    }

    return result

@blueprint.route("/login", methods=["POST"])
@use_args(login_args, location="json")
@orm.db_session
def login(args):
    result = {"error": None, "data": {}}

    if not (account := UserService.get_by_email(args["email"])):
        return abort("account", "not-found")

    if not utils.checkpwd(args["password"], account.password):
        return abort("account", "login-failed")

    account.login = datetime.utcnow()
    login_token = Token.create("login", account.username)
    data = Token.payload(login_token)

    result["data"] = {
        "token": login_token,
        "expire": data["expire"],
        "username": data["meta"]
    }

    return result
