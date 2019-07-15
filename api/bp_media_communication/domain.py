from . import backend
from ..helper_functions.get_media_by_id import get_communication_media_by_id


def create_medias(media_data, communication_id):
    medias = backend.create_medias(media_data, communication_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media(media_communication_id):
    media = get_communication_media_by_id(media_communication_id)
    media_dict = media.to_dict()

    return media_dict


def get_medias(communication_id):
    medias = backend.get_medias(communication_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def update_media(media_data, communication_id, media_communication_id):
    medias = backend.update_media(
        media_data, communication_id, media_communication_id
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(media_communication_id):
    backend.delete_media(media_communication_id)
