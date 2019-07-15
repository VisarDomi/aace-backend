from . import backend
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_user_by_id
from ..helper_functions.constants import ONLY, ADMIN_ONLY


@admin_required
def get_user(user_id):
    user = get_user_by_id(user_id)
    user_dict = user.to_dict(only=ONLY)

    education_medias = []
    user_educations = user.educations.all()
    for education in user_educations:
        for education_media in education.medias:
            education_medias.append(education_media.to_dict())
    user_dict["education_medias"] = education_medias

    experience_medias = []
    user_experiences = user.experiences.all()
    for experience in user_experiences:
        for experience_media in experience.medias:
            experience_medias.append(experience_media.to_dict())
    user_dict["experience_medias"] = experience_medias

    skill_medias = []
    user_skills = user.skills.all()
    for skill in user_skills:
        for skill_media in skill.medias:
            skill_medias.append(skill_media.to_dict())
    user_dict["skill_medias"] = skill_medias

    user_dict["years_of_experience"] = "6"

    return user_dict


def get_blank_users():
    users = backend.get_blank_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_rejected_users():
    users = backend.get_rejected_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_applying_and_reapplying_users():
    users = backend.get_applying_and_reapplying_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_accepted_users():
    users = backend.get_accepted_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_applying_users():
    users = backend.get_applying_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_reapplying_users():
    users = backend.get_reapplying_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_rebutted_users():
    users = backend.get_rebutted_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_accepted_application_users():
    users = backend.get_accepted_application_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_rebutted_payment_users():
    users = backend.get_rebutted_payment_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def get_accepted_payment_users():
    users = backend.get_accepted_payment_users()

    users_list = [user.to_dict(only=ADMIN_ONLY) for user in users]
    return users_list


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    user_dict = user.to_dict(only=ONLY)

    return user_dict


def send_email(email_data, user_id):
    backend.send_email(email_data, user_id)
