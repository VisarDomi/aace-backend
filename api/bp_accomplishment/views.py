from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_accomplishment.json")
@token_auth.login_required
def create_accomplishment(user_id):
    return domain.create_accomplishment(request.json, user_id)


@bp.route("/all", methods=["GET"])
# @token_auth.login_required
def get_accomplishments(user_id):
    return domain.get_all_accomplishments(user_id)


@bp.route("/<accomplishment_id>", methods=["GET"])
# @token_auth.login_required
def get_accomplishment(user_id, accomplishment_id):
    return domain.get_accomplishment_by_id(accomplishment_id)


@bp.route("/<accomplishment_id>", methods=["PUT"])
@schema("/update_accomplishment.json")
@token_auth.login_required
def update_accomplishment(user_id, accomplishment_id):
    return domain.update_accomplishment(request.json, user_id, accomplishment_id)


@bp.route("/<accomplishment_id>", methods=["DELETE"])
@token_auth.login_required
def delete_accomplishment(user_id, accomplishment_id):
    domain.delete_accomplishment(user_id, accomplishment_id)

    return jsonify(
        {"message": "Experience with `id: %s` has been deleted." % accomplishment_id}
    )
