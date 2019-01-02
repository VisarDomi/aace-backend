from flask import request

from ..common.validation import schema

from . import bp
from . import domain



@bp.route('/group', methods=['POST'])
@schema('create_group.json')
def create_group():
    return domain.create_group(request.json)


@bp.route('/groups', methods=['GET'])
def get_groups():
    return domain.get_all_groups()


@bp.route('/group/<group_id>', methods=['GET'])
def get_group(group_id):
    return domain.get_group(group_id)


@bp.route('/group/<group_id>', methods=['PUT'])
@schema('/update_group.json')
def update_group(group_id):
    return domain.update_group(request.json, group_id)

@bp.route('/group/<group_id>/user', methods=['POST'])
def add_user_to_group(group_id):
    return domain.add_user_to_group(request.json, group_id)

@bp.route('/group/<group_id>/user', methods=['DELETE'])
def remove_user_from_group(group_id):
    return domain.remove_user_from_group(request.json, group_id)
    
@bp.route('/group/<group_id>', methods=['DELETE'])
def delete_group(group_id):
    domain.delete_group(group_id)
    return { 'message': 'Group with `id: %s` has been deleted.' % group_id }
