from flask import g
from ..common.models import Payment
from ..common.exceptions import CannotChangeOthersProfile, CannotDeleteOthersPayment
from ..bp_media_payment.backend import delete_media, get_all_medias
from ..helper_functions.get_by_id import get_payment_by_id


def create_payment(payment_data, user_id):
    if int(user_id) == g.current_user.id:
        payment = Payment(**payment_data)
        payment.user = g.current_user
        payment.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return payment


def get_all_payments(user_id):
    payments = Payment.query.filter(Payment.user_id == user_id).all()

    return payments


def update_payment(payment_data, user_id, payment_id):
    if int(user_id) == g.current_user.id:
        payment = get_payment_by_id(payment_id)
        payment.update(**payment_data)
        payment.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return payment


def delete_payment(user_id, payment_id):

    if int(user_id) == g.current_user.id:

        medias = get_all_medias(user_id, payment_id)
        for media in medias:
            delete_media(user_id, media.id)
        payment = get_payment_by_id(payment_id)
        payment.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersPayment(message=msg)
