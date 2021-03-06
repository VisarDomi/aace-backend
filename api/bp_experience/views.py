from flask import request
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_experience.json")
@token_auth.login_required
def create_experience(user_id):

    return domain.create_experience(request.json, user_id)


@bp.route("/all", methods=["GET"])
def get_experiences(user_id):

    return domain.get_experiences(user_id)


@bp.route("/<experience_id>", methods=["GET"])
def get_experience(user_id, experience_id):

    return domain.get_experience(experience_id)


@bp.route("/<experience_id>", methods=["PUT"])
@schema("/update_experience.json")
@token_auth.login_required
def update_experience(user_id, experience_id):

    return domain.update_experience(request.json, user_id, experience_id)


@bp.route("/<experience_id>", methods=["DELETE"])
@token_auth.login_required
def delete_experience(user_id, experience_id):
    domain.delete_experience(user_id, experience_id)

    return {"message": "Experience with `id: %s` has been deleted." % experience_id}
