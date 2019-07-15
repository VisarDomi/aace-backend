from . import backend
from ..helper_functions.get_media_by_id import get_poll_media_by_id


def create_medias(media_data, poll_id):
    medias = backend.create_medias(media_data, poll_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media(media_poll_id):
    media = get_poll_media_by_id(media_poll_id)
    media_dict = media.to_dict()

    return media_dict


def get_medias(poll_id):
    medias = backend.get_medias(poll_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def update_media(media_data, poll_id, media_poll_id):
    medias = backend.update_media(media_data, poll_id, media_poll_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(media_poll_id):
    backend.delete_media(media_poll_id)
