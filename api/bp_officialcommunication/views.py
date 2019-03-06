from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_officialcommunication.json")
@token_auth.login_required
def create_officialcommunication():
    return domain.create_officialcommunication(request.json)


@bp.route("/<officialcommunication_id>", methods=["GET"])
def get_officialcommunication(officialcommunication_id):

    return domain.get_officialcommunication_by_id(officialcommunication_id)


@bp.route("/all", methods=["GET"])
def get_officialcommunications():

    return domain.get_all_officialcommunications()


# order is route, schema, auth
@bp.route("/<officialcommunication_id>", methods=["PUT"])
@schema("/update_officialcommunication.json")
@token_auth.login_required
def update_officialcommunication(officialcommunication_id):

    return domain.update_officialcommunication(request.json, officialcommunication_id)


@bp.route("/<officialcommunication_id>", methods=["DELETE"])
@token_auth.login_required
def delete_officialcommunication(officialcommunication_id):
    domain.delete_officialcommunication(officialcommunication_id)

    return {
        "message": "OrganizationGroup with `id: %s` has been deleted."
        % officialcommunication_id
    }


@bp.route("/<officialcommunication_id>/organizationgroup/all", methods=["GET"])
def get_organizationgroups_from_officialcommunication(officialcommunication_id):
    return domain.get_organizationgroups_from_officialcommunication(
        officialcommunication_id
    )


@bp.route(
    "/<officialcommunication_id>/organizationgroup/<organizationgroup_id>",
    methods=["PUT"],
)
@token_auth.login_required
def add_organizationgroup_to_officialcommunication(
    officialcommunication_id, organizationgroup_id
):
    return domain.add_organizationgroup_to_officialcommunication(
        officialcommunication_id, organizationgroup_id
    )


@bp.route(
    "/<officialcommunication_id>/organizationgroup/<organizationgroup_id>",
    methods=["DELETE"],
)
@token_auth.login_required
def remove_organizationgroup_from_officialcommunication(
    officialcommunication_id, organizationgroup_id
):
    domain.remove_organizationgroup_from_officialcommunication(
        officialcommunication_id, organizationgroup_id
    )
    return {
        "message": f"User with `{organizationgroup_id}` has been removed "
        f"from officialcommunication with `{officialcommunication_id}`."
    }
