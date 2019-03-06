from . import backend


def create_medias(media_data, organizationgroup_id):
    medias = backend.create_medias(media_data, organizationgroup_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media_by_id(organizationgroup_id, media_organizationgroup_id):
    media = backend.get_media_by_id(organizationgroup_id, media_organizationgroup_id)
    media_dict = media.to_dict()

    return media_dict


def get_all_medias(organizationgroup_id):
    medias = backend.get_all_medias(organizationgroup_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def update_media(media_data, organizationgroup_id, media_organizationgroup_id):
    medias = backend.update_media(
        media_data, organizationgroup_id, media_organizationgroup_id
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(organizationgroup_id, media_organizationgroup_id):
    backend.delete_media(organizationgroup_id, media_organizationgroup_id)
