from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route(
    "/media_officialcommunication/<media_officialcommunication_id>", methods=["GET"]
)
@token_auth.login_required
def download_officialcommunication(media_officialcommunication_id):
    return domain.download_officialcommunication(media_officialcommunication_id)
