from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_event.json")
@token_auth.login_required
def create_event():
    return domain.create_event(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_events():
    return domain.get_all_events()


@bp.route("/<event_id>", methods=["GET"])
@token_auth.login_required
def get_event(event_id):
    return domain.get_event_by_id(event_id)


@bp.route("/<event_id>", methods=["PUT"])
@schema("/update_event.json")
@token_auth.login_required
def update_event(event_id):
    return domain.update_event(request.json, event_id)


@bp.route("/<event_id>", methods=["DELETE"])
@token_auth.login_required
def delete_event(event_id):
    domain.delete_event(event_id)

    return jsonify({"message": "Event with `id: %s` has been deleted." % event_id})
