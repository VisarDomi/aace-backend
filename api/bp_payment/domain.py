from . import backend
from ..helper_functions.get_by_id import get_payment_by_id as backend_get_payment_by_id


def create_payment(payment_data, user_id):
    payment = backend.create_payment(payment_data, user_id)
    payment_dict = payment.to_dict()

    return payment_dict


def get_payment_by_id(payment_id):
    payment = backend_get_payment_by_id(payment_id)
    payment_dict = payment.to_dict()

    # medias
    media_payment_ids = []
    for payment_media in payment.medias:
        media_payment_ids.append(payment_media.id)
    payment_dict["media_payment_ids"] = media_payment_ids

    return payment_dict


def get_all_payments(user_id):
    payments = backend.get_all_payments(user_id)
    payments_list = []
    for payment in payments:
        payment_dict = payment.to_dict()

        # medias
        media_payment_ids = []
        for payment_media in payment.medias:
            media_payment_ids.append(payment_media.id)
        payment_dict["media_payment_ids"] = media_payment_ids

        payments_list += [payment_dict]

    return payments_list


def update_payment(payment_data, user_id, payment_id):
    payment = backend.update_payment(payment_data, user_id, payment_id)
    payment_dict = payment.to_dict()

    return payment_dict


def delete_payment(user_id, payment_id):
    backend.delete_payment(user_id, payment_id)
