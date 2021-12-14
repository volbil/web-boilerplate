from datetime import datetime
from .base import db
from pony import orm

class User(db.Entity):
    _table_ = "auth_users"

    created = orm.Optional(datetime, default=datetime.utcnow)
    login = orm.Optional(datetime, default=datetime.utcnow)
    username = orm.Required(str, index=True)
    email = orm.Required(str, index=True)
    password = orm.Required(str)
