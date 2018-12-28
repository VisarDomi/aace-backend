from flask import request

from ..common.validation import schema

from . import bp
from . import domain




@bp.route('/api/user', methods=['POST'])
@schema('create_user.json')
def create_user():
    return domain.create_user(request.json)


@bp.route('/api/users', methods=['GET'])
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
