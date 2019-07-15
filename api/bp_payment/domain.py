from . import backend
from ..helper_functions.get_by_id import get_payment_by_id


def create_payment(payment_data, user_id):
    payment = backend.create_payment(payment_data, user_id)
    payment_dict = payment.to_dict()

    return payment_dict


def get_payment(payment_id):
    payment = get_payment_by_id(payment_id)
    payment_dict = payment.to_dict()

    payment_medias = []
    for payment_media in payment.medias:
        payment_medias.append(payment_media.to_dict())
    payment_dict["payment_medias"] = payment_medias

    return payment_dict


def get_payments(user_id):
    payments = backend.get_payments(user_id)
    payments_list = []
    for payment in payments:
        payment_dict = payment.to_dict()

        payment_medias = []
        for payment_media in payment.medias:
            payment_medias.append(payment_media.to_dict())
        payment_dict["payment_medias"] = payment_medias

        payments_list += [payment_dict]

    return payments_list


def update_payment(payment_data, user_id, payment_id):
    payment = backend.update_payment(payment_data, user_id, payment_id)
    payment_dict = payment.to_dict()

    return payment_dict


def delete_payment(user_id, payment_id):
    backend.delete_payment(user_id, payment_id)
