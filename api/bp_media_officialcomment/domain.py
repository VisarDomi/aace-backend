from . import backend
from ..helper_functions.get_by_id import get_officialcomment_media_by_id


def create_medias(media_data, officialcommunication_id, officialcomment_id):
    medias = backend.create_medias(
        media_data, officialcommunication_id, officialcomment_id
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media_by_id(
    officialcommunication_id, officialcomment_id, media_officialcomment_id
):
    media = get_officialcomment_media_by_id(media_officialcomment_id)
    media_dict = media.to_dict()

    return media_dict


def get_all_medias(officialcommunication_id, officialcomment_id):
    medias = backend.get_all_medias(officialcommunication_id, officialcomment_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def update_media(
    media_data, officialcommunication_id, officialcomment_id, media_officialcomment_id
):
    medias = backend.update_media(
        media_data,
        officialcommunication_id,
        officialcomment_id,
        media_officialcomment_id,
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(
    officialcommunication_id, officialcomment_id, media_officialcomment_id
):
    backend.delete_media(
        officialcommunication_id, officialcomment_id, media_officialcomment_id
    )
