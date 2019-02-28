from flask import g

from . import bp
from ..common.models import User

from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    return {"error message": "@basic_auth.error_handler basic_auth_error"}


@bp.route("/login", methods=["POST"])
@basic_auth.login_required
def login():
    g.current_user.get_token(expires_in=36_000_000)
    user = g.current_user
    user_dict = user.to_dict(exclude=["password_hash"])
    return user_dict


@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    return {"error message": "@token_auth.error_handler token_auth_error"}
