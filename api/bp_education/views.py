from flask import request
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_education.json")
@token_auth.login_required
def create_education(user_id):

    return domain.create_education(request.json, user_id)


@bp.route("/all", methods=["GET"])
def get_educations(user_id):

    return domain.get_educations(user_id)


@bp.route("/<education_id>", methods=["GET"])
def get_education(user_id, education_id):

    return domain.get_education(education_id)


@bp.route("/<education_id>", methods=["PUT"])
@schema("/update_education.json")
@token_auth.login_required
def update_education(user_id, education_id):

    return domain.update_education(request.json, user_id, education_id)


@bp.route("/<education_id>", methods=["DELETE"])
@token_auth.login_required
def delete_education(user_id, education_id):
    domain.delete_education(user_id, education_id)

    return {"message": "Education with `id: %s` has been deleted." % education_id}
