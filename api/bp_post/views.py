from flask import request

from ..common.validation import schema

from . import bp
from . import domain


@bp.route('/post', methods=['POST'])
@schema('create_post.json')
# @auth.login_required
def create_post():
    return domain.create_post(request.json)


@bp.route('/post', methods=['GET'])
def get_posts():
    return domain.get_all_posts()


@bp.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
    return domain.get_post_by_id(post_id)


@bp.route('/post/<post_id>', methods=['PUT'])
@schema('/update_post.json')
def update_post(post_id):
    return domain.update_post(request.json, post_id)


@bp.route('/post/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    domain.delete_post(post_id)

    return {
        'message': 'Post with `id: %s` has been deleted.' % post_id
    }
