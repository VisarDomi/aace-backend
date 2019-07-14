from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaPayment
from ..common.exceptions import CannotDeleteOthersMedia, CannotGetOthersMedia
import os
from ..helper_functions.get_by_id import get_payment_by_id, get_payment_media_by_id


files_payment = UploadSet(
    name="paymentfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def create_medias(media_data, user_id, payment_id):
    medias = []
    if int(user_id) == g.current_user.id:
        if get_payment_by_id(payment_id):
            for file in media_data:
                filename = files_payment.save(file)
                url = files_payment.url(filename)
                media = MediaPayment(filename=filename, url=url)
                payment = get_payment_by_id(payment_id)
                media.payment = payment
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_all_medias(user_id, payment_id):
    if int(user_id) == g.current_user.id or g.current_user.role == "admin":
        medias = MediaPayment.query.filter(
            MediaPayment.payment_id == int(payment_id)
        ).all()
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def update_media(media_data, user_id, payment_id, media_payment_id):
    if int(user_id) == g.current_user.id:
        medias = []
        media = MediaPayment.query.filter(
            MediaPayment.id == media_payment_id
        ).one_or_none()
        for file in media_data:
            if file and media:
                delete_media(user_id, media_payment_id)
                filename = files_payment.save(file)
                url = files_payment.url(filename)
                media = MediaPayment(filename=filename, url=url)
                payment = get_payment_by_id(payment_id)
                media.payment = payment
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/payment"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


def delete_media(user_id, media_payment_id):
    if int(user_id) == g.current_user.id:
        media = get_payment_media_by_id(user_id, media_payment_id)
        file_name = files_payment.path(media.filename)
        if is_file(media.filename):
            os.remove(get_file_path(file_name))
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersMedia(message=msg)
