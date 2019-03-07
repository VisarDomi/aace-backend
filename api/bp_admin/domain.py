from . import backend


def get_user_by_id(user_id):
    user = backend.get_user_by_id(user_id)
    ONLY = [
        "register_status",
        "application_date",
        "id",
        "first_name",
        "last_name",
        "profession",
        "sex",
        "summary",
        "country",
        "email",
        "phone",
        "address",
        "birthday",
        "website",
        "comment_from_administrator",
    ]
    user_dict = user.to_dict(only=ONLY)

    media_education_ids = []
    user_educations = user.educations.all()
    for education in user_educations:
        for education_media in education.medias:
            media_education_ids.append(education_media.id)
    user_dict["media_education_ids"] = media_education_ids

    media_experience_ids = []
    user_experiences = user.experiences.all()
    for experience in user_experiences:
        for experience_media in experience.medias:
            media_experience_ids.append(experience_media.id)
    user_dict["media_experience_ids"] = media_experience_ids

    media_skill_ids = []
    user_skills = user.skills.all()
    for skill in user_skills:
        for skill_media in skill.medias:
            media_skill_ids.append(skill_media.id)
    user_dict["media_skill_ids"] = media_skill_ids

    user_dict["years_of_experience"] = "5"

    return user_dict


def get_approved_users():
    users = backend.get_approved_users()

    users_list = [
        user.to_dict(
            only=["id", "first_name", "last_name", "phone", "email", "register_status"]
        )
        for user in users
    ]
    return users_list


def get_applying_users():
    users = backend.get_applying_users()

    users_list = [
        user.to_dict(
            only=["id", "first_name", "last_name", "phone", "email", "register_status"]
        )
        for user in users
    ]
    return users_list


def get_applying_and_reapplying_users():
    users = backend.get_applying_and_reapplying_users()

    users_list = [
        user.to_dict(
            only=["id", "first_name", "last_name", "phone", "email", "register_status"]
        )
        for user in users
    ]
    return users_list


def get_rejected_users():
    users = backend.get_rejected_users()

    users_list = [
        user.to_dict(
            only=["id", "first_name", "last_name", "phone", "email", "register_status"]
        )
        for user in users
    ]
    return users_list


def get_rebutted_users():
    users = backend.get_rebutted_users()

    users_list = [
        user.to_dict(
            only=["id", "first_name", "last_name", "phone", "email", "register_status"]
        )
        for user in users
    ]
    return users_list


def get_reapplying_users():
    users = backend.get_reapplying_users()

    users_list = [
        user.to_dict(
            only=["id", "first_name", "last_name", "phone", "email", "register_status"]
        )
        for user in users
    ]
    return users_list


def get_blank_users():
    users = backend.get_blank_users()

    users_list = [
        user.to_dict(
            only=["id", "first_name", "last_name", "phone", "email", "register_status"]
        )
        for user in users
    ]
    return users_list


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    ONLY = [
        "register_status",
        "application_date",
        "id",
        "first_name",
        "last_name",
        "profession",
        "sex",
        "summary",
        "country",
        "email",
        "phone",
        "address",
        "birthday",
        "website",
        "comment_from_administrator",
    ]
    user_dict = user.to_dict(only=ONLY)

    return user_dict
