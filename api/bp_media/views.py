from flask import request, jsonify
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_media.json")
@token_auth.login_required
def create_media():
    return domain.create_media(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_medias():
    return domain.get_all_medias()


@bp.route("/<media_id>", methods=["GET"])
@token_auth.login_required
def get_media(media_id):
    return domain.get_media_by_id(media_id)


@bp.route("/<media_id>", methods=["PUT"])
@schema("/update_media.json")
@token_auth.login_required
def update_media(media_id):
    return domain.update_media(request.json, media_id)


@bp.route("/<media_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(media_id):
    domain.delete_media(media_id)

    return jsonify({"message": "Post with `id: %s` has been deleted." % media_id})
