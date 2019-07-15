from . import backend
from ..helper_functions.get_by_id import get_experience_by_id


def create_experience(experience_data, user_id):
    experience = backend.create_experience(experience_data, user_id)
    experience_dict = experience.to_dict()

    return experience_dict


def get_experiences(user_id):
    experiences = backend.get_experiences(user_id)
    experiences_list = []
    for experience in experiences:
        experience_dict = experience.to_dict()

        experience_medias = []
        for experience_media in experience.medias:
            experience_medias.append(experience_media.to_dict())
        experience_dict["experience_medias"] = experience_medias

        experiences_list += [experience_dict]

    return experiences_list


def get_experience(experience_id):
    experience = get_experience_by_id(experience_id)
    experience_dict = experience.to_dict()

    experience_medias = []
    for experience_media in experience.medias:
        experience_medias.append(experience_media.to_dict())
    experience_dict["experience_medias"] = experience_medias

    return experience_dict


def update_experience(experience_data, user_id, experience_id):
    experience = backend.update_experience(experience_data, user_id, experience_id)
    experience_dict = experience.to_dict()

    return experience_dict


def delete_experience(user_id, experience_id):
    backend.delete_experience(user_id, experience_id)
