from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_media_experience.json")
@token_auth.login_required
def create_media(user_id, experience_id):
    return domain.create_media(request.json, user_id, experience_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_medias(user_id, experience_id):
    return domain.get_all_medias()


@bp.route("/<media_id>", methods=["GET"])
@token_auth.login_required
def get_media(user_id, experience_id, media_id):
    return domain.get_media_by_id(media_id)


@bp.route("/<media_id>", methods=["PUT"])
@schema("/update_media_experience.json")
@token_auth.login_required
def update_media(user_id, experience_id, media_id):
    return domain.update_media(request.json, user_id, media_id)


@bp.route("/<media_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(user_id, experience_id, media_id):
    domain.delete_media(media_id)

    return jsonify({"message": "Media with `id: %s` has been deleted." % media_id})
