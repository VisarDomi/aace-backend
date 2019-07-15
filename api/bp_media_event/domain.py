from . import backend
from ..helper_functions.get_media_by_id import get_event_media_by_id


def create_medias(media_data, event_id):
    medias = backend.create_medias(media_data, event_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_medias(event_id):
    medias = backend.get_medias(event_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media(media_event_id):
    media = get_event_media_by_id(media_event_id)
    media_dict = media.to_dict()

    return media_dict


def update_media(media_data, event_id, media_event_id):
    medias = backend.update_media(media_data, event_id, media_event_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(media_event_id):
    backend.delete_media(media_event_id)
