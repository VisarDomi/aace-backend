from flask import request,jsonify,g
from ..common.validation import schema

from . import bp
from . import domain
from ..common.models import User

from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

def get_token():
    pass

def revoke_token():
    pass

@basic_auth.verify_password
def verify_password(email, password):
    print("In verification password I get: ", email, password)
    user = User.query.filter_by(email=email).first()
    print("I got user: ", user)
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)

@basic_auth.error_handler
def basic_auth_error():
    return {"error message":"401"}

@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    g.current_user.save()
    return jsonify({'token': token})


@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None

@token_auth.error_handler
def token_auth_error():
    return {"error message":"401"}
