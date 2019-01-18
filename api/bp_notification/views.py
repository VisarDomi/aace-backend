from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_notification.json")
@token_auth.login_required
def create_notification(user_id):
    return domain.create_notification(request.json, user_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_notifications(user_id):
    return domain.get_all_notifications(user_id)


@bp.route("/<notification_id>", methods=["GET"])
@token_auth.login_required
def get_notification(user_id, notification_id):
    return domain.get_notification_by_id(notification_id)


@bp.route("/<notification_id>", methods=["PUT"])
@schema("/update_notification.json")
@token_auth.login_required
def update_notification(user_id, notification_id):
    return domain.update_notification(request.json, user_id, notification_id)


@bp.route("/<notification_id>", methods=["DELETE"])
@token_auth.login_required
def delete_notification(user_id, notification_id):
    domain.delete_notification(notification_id)

    return jsonify(
        {"message": "Notification with `id: %s` has been deleted." % notification_id}
    )
