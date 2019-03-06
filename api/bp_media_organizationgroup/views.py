from flask import request
from . import bp
from . import domain

from ..bp_auth.views import token_auth


@bp.route("/media", methods=["POST"])
@token_auth.login_required
def create_medias(organizationgroup_id):

    return domain.create_medias(request.files.getlist("file"), organizationgroup_id)


@bp.route("/media/<media_organizationgroup_id>", methods=["GET"])
def get_media(organizationgroup_id, media_organizationgroup_id):

    return domain.get_media_by_id(organizationgroup_id, media_organizationgroup_id)


@bp.route("/media/all", methods=["GET"])
def get_medias(organizationgroup_id):

    return domain.get_all_medias(organizationgroup_id)


@bp.route("/media/<media_organizationgroup_id>", methods=["PUT"])
@token_auth.login_required
def update_media(organizationgroup_id, media_organizationgroup_id):

    return domain.update_media(
        request.files.getlist("file"),
        organizationgroup_id,
        media_organizationgroup_id,
    )


@bp.route("/media/<media_organizationgroup_id>", methods=["DELETE"])
@token_auth.login_required
def delete_media(organizationgroup_id, media_organizationgroup_id):
    domain.delete_media(organizationgroup_id, media_organizationgroup_id)

    return {
        "message": "Media with `id: %s` has been deleted." % media_organizationgroup_id
    }
