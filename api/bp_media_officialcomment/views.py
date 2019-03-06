from flask import request
from . import bp
from . import domain

from ..bp_auth.views import token_auth


@bp.route("/media", methods=["POST"])
@token_auth.login_required
def create_medias(officialcomment_id):

    return domain.create_medias(request.files.getlist("file"), officialcomment_id)


@bp.route("/media/<media_officialcomment_id>", methods=["GET"])
def get_media(officialcomment_id, media_officialcomment_id):

    return domain.get_media_by_id(
        officialcomment_id, media_officialcomment_id
    )


@bp.route("/media/all", methods=["GET"])
def get_medias(officialcomment_id):

    return domain.get_all_medias(officialcomment_id)


@bp.route("/media/<media_officialcomment_id>", methods=["PUT"])
@token_auth.login_required
def update_media(officialcomment_id, media_officialcomment_id):

    return domain.update_media(
        request.files.getlist("file"),
        officialcomment_id,
        media_officialcomment_id,
    )


@bp.route("/media/<media_officialcomment_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(officialcomment_id, media_officialcomment_id):
    domain.delete_media(officialcomment_id, media_officialcomment_id)

    return {
        "message": "Media with `id: %s` has been deleted."
        % media_officialcomment_id
    }
