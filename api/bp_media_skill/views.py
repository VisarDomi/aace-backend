from flask import request
from . import bp
from . import domain

from ..bp_auth.views import token_auth


@bp.route("/media", methods=["POST"])
@token_auth.login_required
def create_medias(user_id, skill_id):

    return domain.create_medias(request.files.getlist("file"), user_id, skill_id)


@bp.route("/media/<media_skill_id>", methods=["GET"])
@token_auth.login_required
def get_media(user_id, skill_id, media_skill_id):

    return domain.get_media(user_id, media_skill_id)


@bp.route("/media/all", methods=["GET"])
@token_auth.login_required
def get_medias(user_id, skill_id):

    return domain.get_medias(user_id, skill_id)


@bp.route("/media/<media_skill_id>", methods=["PUT"])
@token_auth.login_required
def update_media(user_id, skill_id, media_skill_id):

    return domain.update_media(
        request.files.getlist("file"), user_id, skill_id, media_skill_id
    )


@bp.route("/media/<media_skill_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(user_id, skill_id, media_skill_id):
    domain.delete_media(user_id, media_skill_id)

    return {"message": "Media with `id: %s` has been deleted." % media_skill_id}
