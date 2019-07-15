from . import backend
from ..helper_functions.get_media_by_id import get_organizationgroup_media_by_id


def create_medias(media_data, organizationgroup_id):
    medias = backend.create_medias(media_data, organizationgroup_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_medias(organizationgroup_id):
    medias = backend.get_medias(organizationgroup_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media(media_organizationgroup_id):
    media = get_organizationgroup_media_by_id(media_organizationgroup_id)
    media_dict = media.to_dict()

    return media_dict


def update_media(media_data, organizationgroup_id, media_organizationgroup_id):
    medias = backend.update_media(
        media_data, organizationgroup_id, media_organizationgroup_id
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(organizationgroup_id, media_organizationgroup_id):
    backend.delete_media(organizationgroup_id, media_organizationgroup_id)
