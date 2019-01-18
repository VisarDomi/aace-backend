from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_message.json")
@token_auth.login_required
def create_message():
    return domain.create_message(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_messages():
    return domain.get_all_messages()


@bp.route("/<message_id>", methods=["GET"])
@token_auth.login_required
def get_message(message_id):
    return domain.get_message_by_id(message_id)


@bp.route("/<message_id>", methods=["PUT"])
@schema("/update_message.json")
@token_auth.login_required
def update_message(message_id):
    return domain.update_message(request.json, message_id)


@bp.route("/<message_id>", methods=["DELETE"])
@token_auth.login_required
def delete_message(message_id):
    domain.delete_message(message_id)

    return jsonify({"message": "Post with `id: %s` has been deleted." % message_id})
