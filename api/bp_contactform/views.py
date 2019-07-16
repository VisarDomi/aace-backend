from flask import request

from ..common.validation import schema
from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_contactform.json")
def create_contactform():
    return domain.create_contactform(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_contactforms():

    return domain.get_contactforms()


@bp.route("/<contactform_id>", methods=["GET"])
@token_auth.login_required
def get_contactform(contactform_id):

    return domain.get_contactform(contactform_id)


@bp.route("/<contactform_id>", methods=["DELETE"])
@token_auth.login_required
def delete_contactform(contactform_id):
    domain.delete_contactform(contactform_id)

    return {"message": "ContactForm with `id: %s` has been deleted." % contactform_id}
