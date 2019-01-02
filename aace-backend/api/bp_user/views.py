from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth




@bp.route('/api/user', methods=['POST'])
@schema('create_user.json')
def create_user():
    return domain.create_user(request.json)


@bp.route('/api/users', methods=['GET'])
@token_auth.login_required
def get_users():
    return domain.get_all_users()


@bp.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return domain.get_user_by_id(user_id)


@bp.route('/api/user/<user_id>', methods=['PUT'])
@schema('/update_user.json')
def update_user(user_id):
    return domain.update_user(request.json, user_id)

@bp.route('/api/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    domain.delete_user(user_id)

    return {
        'message': 'User with `id: %s` has been deleted.' % user_id
    }

# @bp.route('/api/login', methods=['POST'])
# def login():
#     login_user(user)

# @login_manager.user_loader
# def load_user(user_id):
#     return domain.get_user_object(user_id)