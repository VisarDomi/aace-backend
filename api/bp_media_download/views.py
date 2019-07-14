from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route(
    "/media_communication/<media_communication_id>", methods=["GET"]
)
@token_auth.login_required
def download_communication(media_communication_id):
    return domain.download_communication(media_communication_id)


@bp.route("/media_comment/<media_comment_id>", methods=["GET"])
@token_auth.login_required
def download_comment(media_comment_id):
    return domain.download_comment(media_comment_id)
