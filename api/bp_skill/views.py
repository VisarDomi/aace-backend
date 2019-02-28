from flask import request
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_skill.json")
@token_auth.login_required
def create_skill(user_id):
    return domain.create_skill(request.json, user_id)


@bp.route("/all", methods=["GET"])
def get_skills(user_id):
    return domain.get_all_skills(user_id)


@bp.route("/<skill_id>", methods=["GET"])
def get_skill(user_id, skill_id):
    return domain.get_skill_by_id(skill_id)


@bp.route("/<skill_id>", methods=["PUT"])
@schema("/update_skill.json")
@token_auth.login_required
def update_skill(user_id, skill_id):
    return domain.update_skill(request.json, user_id, skill_id)


@bp.route("/<skill_id>", methods=["DELETE"])
@token_auth.login_required
def delete_skill(user_id, skill_id):
    domain.delete_skill(user_id, skill_id)

    return {"message": "Experience with `id: %s` has been deleted." % skill_id}
