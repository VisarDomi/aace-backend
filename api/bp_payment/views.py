from flask import request
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_payment.json")
@token_auth.login_required
def create_payment(user_id):

    return domain.create_payment(request.json, user_id)


@bp.route("/<payment_id>", methods=["GET"])
def get_payment(user_id, payment_id):

    return domain.get_payment(payment_id)


@bp.route("/all", methods=["GET"])
def get_payments(user_id):

    return domain.get_payments(user_id)


@bp.route("/<payment_id>", methods=["PUT"])
@schema("/update_payment.json")
@token_auth.login_required
def update_payment(user_id, payment_id):

    return domain.update_payment(request.json, user_id, payment_id)


@bp.route("/<payment_id>", methods=["DELETE"])
@token_auth.login_required
def delete_payment(user_id, payment_id):
    domain.delete_payment(user_id, payment_id)

    return {"message": "Payment with `id: %s` has been deleted." % payment_id}
