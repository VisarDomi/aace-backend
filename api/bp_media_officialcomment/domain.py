from . import backend


def create_medias(media_data, officialcomment_id):
    medias = backend.create_medias(media_data, officialcomment_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media_by_id(officialcomment_id, media_officialcomment_id):
    media = backend.get_media_by_id(
        officialcomment_id, media_officialcomment_id
    )
    media_dict = media.to_dict()

    return media_dict


def get_all_medias(officialcomment_id):
    medias = backend.get_all_medias(officialcomment_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def update_media(media_data, officialcomment_id, media_officialcomment_id):
    medias = backend.update_media(
        media_data, officialcomment_id, media_officialcomment_id
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(officialcomment_id, media_officialcomment_id):
    backend.delete_media(officialcomment_id, media_officialcomment_id)
