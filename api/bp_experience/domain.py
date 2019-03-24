from . import backend
from ..helper_functions.get_by_id import (
    get_experience_by_id as backend_get_experience_by_id,
)


def create_experience(experience_data, user_id):
    experience = backend.create_experience(experience_data, user_id)
    experience_dict = experience.to_dict()

    return experience_dict


def get_experience_by_id(experience_id):
    experience = backend_get_experience_by_id(experience_id)
    experience_dict = experience.to_dict()

    media_experience_ids = []
    media_experience = []
    for experience_media in experience.medias:
        media_experience_ids.append(experience_media.id)
        media_experience.append(experience_media.to_dict())
    experience_dict["media_experience_ids"] = media_experience_ids
    experience_dict["media_experience"] = media_experience

    return experience_dict


def get_all_experiences(user_id):
    experiences = backend.get_all_experiences(user_id)
    experiences_list = []
    for experience in experiences:
        experience_dict = experience.to_dict()

        media_experience_ids = []
        media_experience = []
        for experience_media in experience.medias:
            media_experience_ids.append(experience_media.id)
            media_experience.append(experience_media.to_dict())
        experience_dict["media_experience_ids"] = media_experience_ids
        experience_dict["media_experience"] = media_experience

        experiences_list += [experience_dict]

    return experiences_list


def update_experience(experience_data, user_id, experience_id):
    experience = backend.update_experience(experience_data, user_id, experience_id)
    experience_dict = experience.to_dict()

    return experience_dict


def delete_experience(user_id, experience_id):
    backend.delete_experience(user_id, experience_id)
