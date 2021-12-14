from ..decorators import auth_required
from flask import Blueprint, request
from pony import orm

blueprint = Blueprint("profile", __name__, url_prefix="/profile")

@blueprint.route("/info", methods=["GET"])
@orm.db_session
@auth_required
def info():
    return {
        "error": None, "data": {
            "username": request.account.username,
            "email": request.account.email
        }
    }
