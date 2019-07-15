from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_poll.json")
@token_auth.login_required
def create_poll():
    return domain.create_poll(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_polls():

    return domain.get_polls()


@bp.route("/<poll_id>", methods=["GET"])
@token_auth.login_required
def get_poll(poll_id):

    return domain.get_poll(poll_id)


# order is route, schema, auth
@bp.route("/<poll_id>", methods=["PUT"])
@schema("/update_poll.json")
@token_auth.login_required
def update_poll(poll_id):

    return domain.update_poll(request.json, poll_id)


@bp.route("/<poll_id>", methods=["DELETE"])
@token_auth.login_required
def delete_poll(poll_id):
    domain.delete_poll(poll_id)

    return {"message": "Communication with `id: %s` has been deleted." % poll_id}


@bp.route("/<poll_id>/organizationgroup/all", methods=["GET"])
@token_auth.login_required
def get_organizationgroups_from_poll(poll_id):

    return domain.get_organizationgroups_from_poll(poll_id)


@bp.route("/<poll_id>/organizationgroup/<organizationgroup_id>", methods=["PUT"])
@token_auth.login_required
def add_organizationgroup_to_poll(poll_id, organizationgroup_id):

    return domain.add_organizationgroup_to_poll(poll_id, organizationgroup_id)


@bp.route("/<poll_id>/organizationgroup/<organizationgroup_id>", methods=["DELETE"])
@token_auth.login_required
def remove_organizationgroup_from_poll(poll_id, organizationgroup_id):
    domain.remove_organizationgroup_from_poll(poll_id, organizationgroup_id)

    return {
        "message": (
            f"Organizationgroup with id `{organizationgroup_id}` has been "
            f"removed from poll with id `{poll_id}`."
        )
    }


@bp.route("/<poll_id>/email", methods=["POST"])
@token_auth.login_required
def send_email(poll_id):
    domain.send_email(poll_id)

    return {
        "message": (
            f"An email has been sent to all members of the groups of the "
            f"official poll with id `{poll_id}`"
        )
    }
