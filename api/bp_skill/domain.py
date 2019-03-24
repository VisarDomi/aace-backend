from . import backend
from ..helper_functions.get_by_id import get_skill_by_id as backend_get_skill_by_id


def create_skill(skill_data, user_id):
    skill = backend.create_skill(skill_data, user_id)
    skill_dict = skill.to_dict()

    return skill_dict


def get_skill_by_id(skill_id):
    skill = backend_get_skill_by_id(skill_id)
    skill_dict = skill.to_dict()

    skill_medias = []
    for skill_media in skill.medias:
        skill_medias.append(skill_media.to_dict())
    skill_dict["skill_medias"] = skill_medias

    return skill_dict


def get_all_skills(user_id):
    skills = backend.get_all_skills(user_id)
    skills_list = []
    for skill in skills:
        skill_dict = skill.to_dict()

        skill_medias = []
        for skill_media in skill.medias:
            skill_medias.append(skill_media.to_dict())
        skill_dict["skill_medias"] = skill_medias

        skills_list += [skill_dict]

    return skills_list


def update_skill(skill_data, user_id, skill_id):
    skill = backend.update_skill(skill_data, user_id, skill_id)
    skill_dict = skill.to_dict()

    return skill_dict


def delete_skill(user_id, skill_id):
    backend.delete_skill(user_id, skill_id)
