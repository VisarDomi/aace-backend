from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("/comment/<comment_id>/media", methods=["POST"])
@bp.route("/event/<event_id>/media", methods=["POST"])
@bp.route("/experience/<experience_id>/media", methods=["POST"])
@bp.route("/message/<message_id>/media", methods=["POST"])
@bp.route("/post/<post_id>/media", methods=["POST"])
@schema("create_media.json")
@token_auth.login_required
def create_media(
    user_id, comment_id=0, event_id=0, experience_id=0, message_id=0, post_id=0
):
    return domain.create_media(
        request.json, comment_id, event_id, experience_id, message_id, post_id
    )


@bp.route("/comment/<comment_id>/media/all", methods=["GET"])
@bp.route("/event/<event_id>/media/all", methods=["GET"])
@bp.route("/experience/<experience_id>/media/all", methods=["GET"])
@bp.route("/message/<message_id>/media/all", methods=["GET"])
@bp.route("/post/<post_id>/media/all", methods=["GET"])
@token_auth.login_required
def get_medias(
    user_id, comment_id=0, event_id=0, experience_id=0, message_id=0, post_id=0
):
    return domain.get_all_medias(
        comment_id, event_id, experience_id, message_id, post_id
    )


@bp.route("/comment/<comment_id>/media/<media_id>", methods=["GET"])
@bp.route("/event/<event_id>/media/<media_id>", methods=["GET"])
@bp.route("/experience/<experience_id>/media/<media_id>", methods=["GET"])
@bp.route("/message/<message_id>/media/<media_id>", methods=["GET"])
@bp.route("/post/<post_id>/media/<media_id>", methods=["GET"])
@token_auth.login_required
def get_media(
    user_id,
    media_id,
    comment_id=0,
    event_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    return domain.get_media_by_id(media_id)


@bp.route("/comment/<comment_id>/media/<media_id>", methods=["PUT"])
@bp.route("/event/<event_id>/media/<media_id>", methods=["PUT"])
@bp.route("/experience/<experience_id>/media/<media_id>", methods=["PUT"])
@bp.route("/message/<message_id>/media/<media_id>", methods=["PUT"])
@bp.route("/post/<post_id>/media/<media_id>", methods=["PUT"])
@schema("/update_media.json")
@token_auth.login_required
def update_media(
    user_id,
    media_id,
    comment_id=0,
    event_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    return domain.update_media(request.json, user_id, media_id)


@bp.route("/comment/<comment_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/event/<event_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/experience/<experience_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/message/<message_id>/media/<media_id>", methods=["DELETE"])
@bp.route("/post/<post_id>/media/<media_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(
    user_id,
    media_id,
    comment_id=0,
    event_id=0,
    experience_id=0,
    message_id=0,
    post_id=0,
):
    domain.delete_media(media_id)

    return jsonify({"message": "Media with `id: %s` has been deleted." % media_id})