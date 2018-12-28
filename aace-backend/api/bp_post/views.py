from flask import request

from ..common.validation import schema

from . import bp
from . import domain


@bp.route('/api/post', methods=['POST'])
@schema('create_post.json')
# @auth.login_required
def create_post():
    return domain.create_post(request.json)


# @bp.route('/foss', methods=['GET'])
# def get_fosses():
#     return domain.get_all_fosses()


# @bp.route('/foss/<foss_id>', methods=['GET'])
# def get_foss(foss_id):
#     return domain.get_foss_by_id(foss_id)


# @bp.route('/foss/<foss_id>', methods=['PUT'])
# @schema('/update_foss.json')
# def update_foss(foss_id):
#     return domain.update_foss(request.json, foss_id)


# @bp.route('/foss/<foss_id>', methods=['DELETE'])
# def delete_foss(foss_id):
#     domain.delete_foss(foss_id)

#     return {
#         'message': 'Foss with `id: %s` has been deleted.' % foss_id
#     }
