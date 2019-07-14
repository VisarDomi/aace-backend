from . import backend
from ..helper_functions.get_by_id import get_comment_media_by_id


def create_medias(media_data, communication_id, comment_id):
    medias = backend.create_medias(
        media_data, communication_id, comment_id
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media_by_id(
    communication_id, comment_id, media_comment_id
):
    media = get_comment_media_by_id(media_comment_id)
    media_dict = media.to_dict()

    return media_dict


def get_all_medias(communication_id, comment_id):
    medias = backend.get_all_medias(communication_id, comment_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def update_media(
    media_data, communication_id, comment_id, media_comment_id
):
    medias = backend.update_media(
        media_data,
        communication_id,
        comment_id,
        media_comment_id,
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(
    communication_id, comment_id, media_comment_id
):
    backend.delete_media(
        communication_id, comment_id, media_comment_id
    )
