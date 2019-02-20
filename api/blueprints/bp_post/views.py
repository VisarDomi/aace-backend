from flask import request, jsonify
from . import bp
from . import domain
from ...common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_post.json")
@token_auth.login_required
def create_post(user_id):
    return domain.create_post(request.json, user_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_posts(user_id):
    return domain.get_all_posts(user_id)


@bp.route("/<post_id>", methods=["GET"])
@token_auth.login_required
def get_post(user_id, post_id):
    return domain.get_post_by_id(post_id)


@bp.route("/<post_id>", methods=["PUT"])
@schema("/update_post.json")
@token_auth.login_required
def update_post(user_id, post_id):
    return domain.update_post(request.json, user_id, post_id)


@bp.route("/<post_id>", methods=["DELETE"])
@token_auth.login_required
def delete_post(user_id, post_id):
    domain.delete_post(user_id, post_id)

    return jsonify({"message": "Post with `id: %s` has been deleted." % post_id})
