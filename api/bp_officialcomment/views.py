from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_officialcomment.json")
@token_auth.login_required
def create_officialcomment(officialcommunication_id):
    return domain.create_officialcomment(request.json, officialcommunication_id)


@bp.route("/<officialcomment_id>", methods=["GET"])
@token_auth.login_required
def get_officialcomment(officialcommunication_id, officialcomment_id):

    return domain.get_officialcomment_by_id(
        officialcommunication_id, officialcomment_id
    )


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_officialcomments(officialcommunication_id):

    return domain.get_all_officialcomments(officialcommunication_id)


# order is route, schema, auth
@bp.route("/<officialcomment_id>", methods=["PUT"])
@schema("/update_officialcomment.json")
@token_auth.login_required
def update_officialcomment(officialcommunication_id, officialcomment_id):

    return domain.update_officialcomment(
        request.json, officialcommunication_id, officialcomment_id
    )


@bp.route("/<officialcomment_id>", methods=["DELETE"])
@token_auth.login_required
def delete_officialcomment(officialcommunication_id, officialcomment_id):
    domain.delete_officialcomment(officialcommunication_id, officialcomment_id)

    return {
        "message": "OrganizationComment with `id: %s` has been deleted."
        % officialcomment_id
    }
