from flask import request
from . import bp
from . import domain

from ..bp_auth.views import token_auth


@bp.route("/media", methods=["POST"])
@token_auth.login_required
def create_medias(poll_id):

    return domain.create_medias(request.files.getlist("file"), poll_id)


@bp.route("/media/<media_poll_id>", methods=["GET"])
@token_auth.login_required
def get_media(poll_id, media_poll_id):

    return domain.get_media(media_poll_id)


@bp.route("/media/all", methods=["GET"])
@token_auth.login_required
def get_medias(poll_id):

    return domain.get_medias(poll_id)


@bp.route("/media/<media_poll_id>", methods=["PUT"])
@token_auth.login_required
def update_media(poll_id, media_poll_id):

    return domain.update_media(request.files.getlist("file"), poll_id, media_poll_id)


@bp.route("/media/<media_poll_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(poll_id, media_poll_id):
    domain.delete_media(media_poll_id)

    return {"message": "Media with `id: %s` has been deleted." % media_poll_id}
