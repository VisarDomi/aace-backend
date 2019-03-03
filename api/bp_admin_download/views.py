from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("/media_education/<media_education_id>", methods=["GET"])
@token_auth.login_required
def download_education(media_education_id):
    return domain.download_education(media_education_id)


@bp.route("/media_experience/<media_experience_id>", methods=["GET"])
@token_auth.login_required
def download_experience(media_experience_id):
    return domain.download_experience(media_experience_id)


@bp.route("/media_skill/<media_skill_id>", methods=["GET"])
@token_auth.login_required
def download_skill(media_skill_id):
    return domain.download_skill(media_skill_id)
