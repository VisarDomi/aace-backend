from flask import request, jsonify

from ...common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("/user/all", methods=["GET"])
@token_auth.login_required
def get_users():
    return domain.get_all_users()


@bp.route("/user/applying", methods=["GET"])
@token_auth.login_required
def get_applying_users():
    return domain.get_applying_users()


@bp.route("/user/<user_id>", methods=["GET"])
@token_auth.login_required
def get_user(user_id):
    return domain.get_user_by_id(user_id)


# order is route, schema, auth
@bp.route("/user/<user_id>", methods=["PUT"])
@schema("/update_user.json")
@token_auth.login_required
def update_user(user_id):
    return domain.update_user(request.json, user_id)


@bp.route("/user/<user_id>", methods=["DELETE"])
@token_auth.login_required
def delete_user(user_id):
    domain.delete_user(user_id)
    return jsonify({"message": "User with `id: %s` has been deleted." % user_id})


@bp.route("/media/<media_id>", methods=["GET"])
@token_auth.login_required
def download(media_id):
    return domain.download(media_id)
