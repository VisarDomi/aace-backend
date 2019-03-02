from . import backend


def create_media(
    media_data,
    user_id,
    skill_id,
    comment_id,
    event_id,
    education_id,
    experience_id,
    message_id,
    post_id,
):
    medias = backend.create_media(
        media_data,
        user_id,
        skill_id,
        comment_id,
        event_id,
        education_id,
        experience_id,
        message_id,
        post_id,
    )
    medias_list = [media.to_dict() for media in medias]
    return medias_list


def get_media_by_id(media_id):
    media = backend.get_media_by_id(media_id)
    media_dict = media.to_dict()
    return media_dict


def get_all_medias(
    user_id,
    skill_id,
    comment_id,
    education_id,
    event_id,
    experience_id,
    message_id,
    post_id,
):
    medias = backend.get_all_medias(
        user_id,
        skill_id,
        comment_id,
        education_id,
        event_id,
        experience_id,
        message_id,
        post_id,
    )
    medias_list = [media.to_dict() for media in medias]
    return medias_list


def update_media(
    media_data,
    user_id,
    media_id,
    skill_id,
    comment_id,
    event_id,
    education_id,
    experience_id,
    message_id,
    post_id,
):
    medias = backend.update_media(
        media_data,
        user_id,
        media_id,
        skill_id,
        comment_id,
        event_id,
        education_id,
        experience_id,
        message_id,
        post_id,
    )
    medias_list = [media.to_dict() for media in medias]
    return medias_list


def delete_media_user(user_id, media_id):
    backend.delete_media_user(user_id, media_id)


def delete_media_education(user_id, education_id, media_id):
    backend.delete_media_education(user_id, education_id, media_id)
