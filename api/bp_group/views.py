from flask import request, jsonify

from ..common.validation import schema

from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_group.json")
@token_auth.login_required
def create_group():
    return domain.create_group(request.json)


@bp.route("/all", methods=["GET"])
def get_groups():
    return domain.get_all_groups()


@bp.route("/<group_id>", methods=["GET"])
def get_group(group_id):
    return domain.get_group_by_id(group_id)


@bp.route("/<group_id>", methods=["PUT"])
@schema("/update_group.json")
@token_auth.login_required
def update_group(group_id):
    return domain.update_group(request.json, group_id)


@bp.route("/<group_id>", methods=["DELETE"])
@token_auth.login_required
def delete_group(group_id):
    domain.delete_group(group_id)
    return jsonify({"message": "Group with `id: %s` has been deleted." % group_id})


@bp.route("/<group_id>/user/<user_id>", methods=["PUT"])
@token_auth.login_required
def add_user_to_group(group_id, user_id):
    return domain.add_user_to_group(group_id, user_id)


@bp.route("/<group_id>/user/<user_id>", methods=["DELETE"])
@token_auth.login_required
def remove_user_from_group(group_id, user_id):
    domain.remove_user_from_group(group_id, user_id)
    return jsonify({"message": "User with `id: %s` has been removed from group with `id: %s`." % (user_id, group_id)})
