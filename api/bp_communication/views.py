from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_communication.json")
@token_auth.login_required
def create_communication():
    return domain.create_communication(request.json)


@bp.route("/<communication_id>", methods=["GET"])
@token_auth.login_required
def get_communication(communication_id):

    return domain.get_communication_by_id(communication_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_communications():

    return domain.get_all_communications()


# order is route, schema, auth
@bp.route("/<communication_id>", methods=["PUT"])
@schema("/update_communication.json")
@token_auth.login_required
def update_communication(communication_id):

    return domain.update_communication(request.json, communication_id)


@bp.route("/<communication_id>", methods=["DELETE"])
@token_auth.login_required
def delete_communication(communication_id):
    domain.delete_communication(communication_id)

    return {
        "message": "OrganizationGroup with `id: %s` has been deleted."
        % communication_id
    }


@bp.route("/<communication_id>/organizationgroup/all", methods=["GET"])
@token_auth.login_required
def get_organizationgroups_from_communication(communication_id):

    return domain.get_organizationgroups_from_communication(
        communication_id
    )


@bp.route(
    "/<communication_id>/organizationgroup/<organizationgroup_id>",
    methods=["PUT"],
)
@token_auth.login_required
def add_organizationgroup_to_communication(
    communication_id, organizationgroup_id
):

    return domain.add_organizationgroup_to_communication(
        communication_id, organizationgroup_id
    )


@bp.route(
    "/<communication_id>/organizationgroup/<organizationgroup_id>",
    methods=["DELETE"],
)
@token_auth.login_required
def remove_organizationgroup_from_communication(
    communication_id, organizationgroup_id
):
    domain.remove_organizationgroup_from_communication(
        communication_id, organizationgroup_id
    )

    return {
        "message": (
            f"Organizationgroup with id `{organizationgroup_id}` has been "
            f"removed from communication with id `{communication_id}`."
        )
    }


@bp.route("/<communication_id>/email", methods=["POST"])
@token_auth.login_required
def send_email(communication_id):
    domain.send_email(communication_id)

    return {
        "message": (
            f"An email has been sent to all members of the groups of the "
            f"official communication with id `{communication_id}`"
        )
    }
