from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("/approved", methods=["GET"])
@token_auth.login_required
def get_approved_users():
    return domain.get_approved_users()


@bp.route("/applying", methods=["GET"])
@token_auth.login_required
def get_applying_users():
    return domain.get_applying_users()


@bp.route("/applying_and_reapplying", methods=["GET"])
@token_auth.login_required
def get_applying_and_reapplying_users():
    return domain.get_applying_and_reapplying_users()


@bp.route("/rejected", methods=["GET"])
@token_auth.login_required
def get_rejected_users():
    return domain.get_rejected_users()


@bp.route("/rebutted", methods=["GET"])
@token_auth.login_required
def get_rebutted_users():
    return domain.get_rebutted_users()


@bp.route("/reapplying", methods=["GET"])
@token_auth.login_required
def get_reapplying_users():
    return domain.get_reapplying_users()


@bp.route("/blank", methods=["GET"])
@token_auth.login_required
def get_blank_users():
    return domain.get_blank_users()


@bp.route("/<user_id>", methods=["GET"])
@token_auth.login_required
def get_user(user_id):
    return domain.get_user_by_id(user_id)


# order is route, schema, auth
@bp.route("/<user_id>", methods=["PUT"])
@schema("/update_user.json")
@token_auth.login_required
def update_user(user_id):
    return domain.update_user(request.json, user_id)
