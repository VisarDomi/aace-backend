from flask import request
from . import bp
from . import domain

from ..bp_auth.views import token_auth


@bp.route("/accomplishment/<accomplishment_id>/media", methods=["POST"])
@bp.route("/comment/<comment_id>/media", methods=["POST"])
@bp.route("/education/<education_id>/media", methods=["POST"])
@bp.route("/event/<event_id>/media", methods=["POST"])
@bp.route("/experience/<experience_id>/media", methods=["POST"])
@bp.route("/message/<message_id>/media", methods=["POST"])
@bp.route("/post/<post_id>/media", methods=["POST"])
@bp.route("/media", methods=["POST"])
@token_auth.login_required
def create_media(
    user_id,
    accomplishment_id=0,
    comment_id=0,
    event_id=0,
    education_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    return domain.create_media(
        request.files.getlist("file"),
        user_id,
        accomplishment_id,
        comment_id,
        event_id,
        education_id,
        experience_id,
        message_id,
        post_id,
    )


@bp.route("/accomplishment/<accomplishment_id>/media/all", methods=["GET"])
@bp.route("/comment/<comment_id>/media/all", methods=["GET"])
@bp.route("/education/<education_id>/media/all", methods=["GET"])
@bp.route("/event/<event_id>/media/all", methods=["GET"])
@bp.route("/experience/<experience_id>/media/all", methods=["GET"])
@bp.route("/message/<message_id>/media/all", methods=["GET"])
@bp.route("/post/<post_id>/media/all", methods=["GET"])
@bp.route("/media/all", methods=["GET"])
@token_auth.login_required
def get_medias(
    user_id,
    accomplishment_id=0,
    comment_id=0,
    event_id=0,
    education_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    return domain.get_all_medias(
        user_id,
        accomplishment_id,
        comment_id,
        education_id,
        event_id,
        experience_id,
        message_id,
        post_id,
    )


@bp.route("/accomplishment/<accomplishment_id>/media/<media_id>", methods=["GET"])
@bp.route("/comment/<comment_id>/media/<media_id>", methods=["GET"])
@bp.route("/education/<education_id>/media/<media_id>", methods=["GET"])
@bp.route("/event/<event_id>/media/<media_id>", methods=["GET"])
@bp.route("/experience/<experience_id>/media/<media_id>", methods=["GET"])
@bp.route("/message/<message_id>/media/<media_id>", methods=["GET"])
@bp.route("/post/<post_id>/media/<media_id>", methods=["GET"])
@bp.route("/media/<media_id>", methods=["GET"])
@token_auth.login_required
def get_media(
    user_id,
    media_id,
    accomplishment_id=0,
    comment_id=0,
    event_id=0,
    education_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    return domain.get_media_by_id(media_id)


@bp.route("/accomplishment/<accomplishment_id>/media/<media_id>", methods=["PUT"])
@bp.route("/comment/<comment_id>/media/<media_id>", methods=["PUT"])
@bp.route("/education/<education_id>/media/<media_id>", methods=["PUT"])
@bp.route("/event/<event_id>/media/<media_id>", methods=["PUT"])
@bp.route("/experience/<experience_id>/media/<media_id>", methods=["PUT"])
@bp.route("/message/<message_id>/media/<media_id>", methods=["PUT"])
@bp.route("/post/<post_id>/media/<media_id>", methods=["PUT"])
@bp.route("/media/<media_id>", methods=["PUT"])
@token_auth.login_required
def update_media(
    user_id,
    media_id,
    accomplishment_id=0,
    comment_id=0,
    event_id=0,
    education_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    return domain.update_media(
        request.files.getlist("file"),
        user_id,
        media_id,
        accomplishment_id,
        comment_id,
        event_id,
        education_id,
        experience_id,
        message_id,
        post_id,
    )


@bp.route("/accomplishment/<accomplishment_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/comment/<comment_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/education/<education_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/event/<event_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/experience/<experience_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/message/<message_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/post/<post_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/media/<media_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(
    user_id,
    media_id,
    accomplishment_id=0,
    comment_id=0,
    event_id=0,
    education_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    domain.delete_media(user_id, media_id)

    return {"message": "Media with `id: %s` has been deleted." % media_id}
