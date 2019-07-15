from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_user.json")
def create_user():
    return domain.create_user(request.json)


@bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):

    return domain.get_user(user_id)


@bp.route("/all", methods=["GET"])
def get_users():

    return domain.get_users()


# order is route, schema, auth
@bp.route("/<user_id>", methods=["PUT"])
@schema("/update_user.json")
@token_auth.login_required
def update_user(user_id):

    return domain.update_user(request.json, user_id)


@bp.route("/<user_id>", methods=["DELETE"])
@token_auth.login_required
def delete_user(user_id):
    domain.delete_user(user_id)

    return {"message": "User with `id: %s` has been deleted." % user_id}
