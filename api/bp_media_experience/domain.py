from . import backend


def create_medias(media_data, user_id, experience_id):
    medias = backend.create_medias(media_data, user_id, experience_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def get_media_by_id(user_id, media_experience_id):
    media = backend.get_media_by_id(user_id, media_experience_id)
    media_dict = media.to_dict()

    return media_dict


def get_all_medias(user_id, experience_id):
    medias = backend.get_all_medias(user_id, experience_id)
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def update_media(media_data, user_id, experience_id, media_experience_id):
    medias = backend.update_media(
        media_data, user_id, experience_id, media_experience_id
    )
    medias_list = [media.to_dict() for media in medias]

    return medias_list


def delete_media(user_id, media_experience_id):
    backend.delete_media(user_id, media_experience_id)
