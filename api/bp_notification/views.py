from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_notification.json")
@token_auth.login_required
def create_notification():
    return domain.create_notification(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_notifications():
    return domain.get_all_notifications()


@bp.route("/<notification_id>", methods=["GET"])
@token_auth.login_required
def get_notification(notification_id):
    return domain.get_notification_by_id(notification_id)


@bp.route("/<notification_id>", methods=["PUT"])
@schema("/update_notification.json")
@token_auth.login_required
def update_notification(notification_id):
    return domain.update_notification(request.json, notification_id)


@bp.route("/<notification_id>", methods=["DELETE"])
@token_auth.login_required
def delete_notification(notification_id):
    domain.delete_notification(notification_id)

    return jsonify({"notification": "Post with `id: %s` has been deleted." % notification_id})
