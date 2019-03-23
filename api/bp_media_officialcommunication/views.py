from flask import request
from . import bp
from . import domain

from ..bp_auth.views import token_auth


@bp.route("/media", methods=["POST"])
@token_auth.login_required
def create_medias(officialcommunication_id):
    print('request.files.getlist("file"), officialcommunication_id :', request.files.getlist("file"), officialcommunication_id)
    return domain.create_medias(request.files.getlist("file"), officialcommunication_id)


@bp.route("/media/<media_officialcommunication_id>", methods=["GET"])
@token_auth.login_required
def get_media(officialcommunication_id, media_officialcommunication_id):

    return domain.get_media_by_id(media_officialcommunication_id)


@bp.route("/media/all", methods=["GET"])
@token_auth.login_required
def get_medias(officialcommunication_id):

    return domain.get_all_medias(officialcommunication_id)


@bp.route("/media/<media_officialcommunication_id>", methods=["PUT"])
@token_auth.login_required
def update_media(officialcommunication_id, media_officialcommunication_id):

    return domain.update_media(
        request.files.getlist("file"),
        officialcommunication_id,
        media_officialcommunication_id,
    )


@bp.route("/media/<media_officialcommunication_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(officialcommunication_id, media_officialcommunication_id):
    domain.delete_media(media_officialcommunication_id)

    return {
        "message": "Media with `id: %s` has been deleted."
        % media_officialcommunication_id
    }
