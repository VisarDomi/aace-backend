from flask import request

from ..common.validation import schema
from . import bp
from . import domain
# from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("search_users.json")
def search_users():
    return domain.search_users(request.json)
