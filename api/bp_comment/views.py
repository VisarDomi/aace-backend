from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_comment.json")
@token_auth.login_required
def create_comment(communication_id):
    return domain.create_comment(request.json, communication_id)


@bp.route("/<comment_id>", methods=["GET"])
@token_auth.login_required
def get_comment(communication_id, comment_id):

    return domain.get_comment_by_id(
        communication_id, comment_id
    )


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_comments(communication_id):

    return domain.get_all_comments(communication_id)


# order is route, schema, auth
@bp.route("/<comment_id>", methods=["PUT"])
@schema("/update_comment.json")
@token_auth.login_required
def update_comment(communication_id, comment_id):

    return domain.update_comment(
        request.json, communication_id, comment_id
    )


@bp.route("/<comment_id>", methods=["DELETE"])
@token_auth.login_required
def delete_comment(communication_id, comment_id):
    domain.delete_comment(communication_id, comment_id)

    return {
        "message": "OrganizationComment with `id: %s` has been deleted."
        % comment_id
    }
