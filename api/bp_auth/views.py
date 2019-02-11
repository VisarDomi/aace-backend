from flask import jsonify, g

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
    return jsonify({"error message": "basic_auth_error"})


@bp.route("/login", methods=["POST"])
@basic_auth.login_required
def get_token():
    user = g.current_user
    return user.to_json(max_nesting=1)


@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    return jsonify({"error message": "token_auth_error"})
