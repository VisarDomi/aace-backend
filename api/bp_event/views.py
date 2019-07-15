from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_event.json")
@token_auth.login_required
def create_event():
    return domain.create_event(request.json)


@bp.route("/<event_id>", methods=["GET"])
@token_auth.login_required
def get_event(event_id):

    return domain.get_event(event_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_events():

    return domain.get_events()


# order is route, schema, auth
@bp.route("/<event_id>", methods=["PUT"])
@schema("/update_event.json")
@token_auth.login_required
def update_event(event_id):

    return domain.update_event(request.json, event_id)


@bp.route("/<event_id>", methods=["DELETE"])
@token_auth.login_required
def delete_event(event_id):
    domain.delete_event(event_id)

    return {"message": "Event with `id: %s` has been deleted." % event_id}


@bp.route("/<event_id>/organizationgroup/all", methods=["GET"])
@token_auth.login_required
def get_organizationgroups_from_event(event_id):

    return domain.get_organizationgroups_from_event(event_id)


@bp.route("/<event_id>/organizationgroup/<organizationgroup_id>", methods=["PUT"])
@token_auth.login_required
def add_organizationgroup_to_event(event_id, organizationgroup_id):

    return domain.add_organizationgroup_to_event(event_id, organizationgroup_id)


@bp.route("/<event_id>/organizationgroup/<organizationgroup_id>", methods=["DELETE"])
@token_auth.login_required
def remove_organizationgroup_from_event(event_id, organizationgroup_id):
    domain.remove_organizationgroup_from_event(event_id, organizationgroup_id)

    return {
        "message": (
            f"Organizationgroup with id `{organizationgroup_id}` has been "
            f"removed from event with id `{event_id}`."
        )
    }


@bp.route("/<event_id>/email", methods=["POST"])
@token_auth.login_required
def send_email(event_id):
    domain.send_email(event_id)

    return {
        "message": (
            f"An email has been sent to all members of the groups of the "
            f"official event with id `{event_id}`"
        )
    }
