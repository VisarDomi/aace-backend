from . import backend
from ..helper_functions.get_media_by_id import get_user_media_by_id


def create_medias(media_data, user_id):
    medias = backend.create_medias(media_data, user_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_medias(user_id):
    medias = backend.get_medias(user_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media(media_user_id):
    media = get_user_media_by_id(media_user_id)
    media_dict = media.to_dict()

    return media_dict


def update_media(media_data, user_id, media_user_id):
    medias = backend.update_media(media_data, user_id, media_user_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(user_id, media_user_id):
    backend.delete_media(user_id, media_user_id)
