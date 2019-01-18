from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_comment.json")
@token_auth.login_required
def create_comment():
    return domain.create_comment(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_comments():
    return domain.get_all_comments()


@bp.route("/<comment_id>", methods=["GET"])
@token_auth.login_required
def get_comment(comment_id):
    return domain.get_comment_by_id(comment_id)


@bp.route("/<comment_id>", methods=["PUT"])
@schema("/update_comment.json")
@token_auth.login_required
def update_comment(comment_id):
    return domain.update_comment(request.json, comment_id)


@bp.route("/<comment_id>", methods=["DELETE"])
@token_auth.login_required
def delete_comment(comment_id):
    domain.delete_comment(comment_id)

    return jsonify({"message": "Comment with `id: %s` has been deleted." % comment_id})
