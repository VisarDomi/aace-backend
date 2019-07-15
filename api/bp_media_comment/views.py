from flask import request
from . import bp
from . import domain

from ..bp_auth.views import token_auth


@bp.route("/media", methods=["POST"])
@token_auth.login_required
def create_medias(comment_id):

    return domain.create_medias(request.files.getlist("file"), comment_id)


@bp.route("/media/all", methods=["GET"])
@token_auth.login_required
def get_medias(comment_id):

    return domain.get_medias(comment_id)


@bp.route("/media/<media_comment_id>", methods=["GET"])
@token_auth.login_required
def get_media(comment_id, media_comment_id):

    return domain.get_media(comment_id, media_comment_id)


@bp.route("/media/<media_comment_id>", methods=["PUT"])
@token_auth.login_required
def update_media(comment_id, media_comment_id):

    return domain.update_media(
        request.files.getlist("file"), comment_id, media_comment_id
    )


@bp.route("/media/<media_comment_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(comment_id, media_comment_id):
    domain.delete_media(comment_id, media_comment_id)

    return {"message": "Media with `id: %s` has been deleted." % media_comment_id}
