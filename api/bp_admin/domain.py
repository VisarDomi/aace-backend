from . import backend


def get_user_by_id(user_id):
    user = backend.get_user_by_id(user_id)
    ONLY = [
        "id",
        "first_name",
        "last_name",
        "headline",
        "summary",
        "country",
        "industry",
        "email",
        "phone",
        "address",
        "birthday",
        "website",
        "comment_from_administrator",
    ]
    user_dict = user.to_dict(only=ONLY)

    user_documents = []
    user_educations = user.educations.all()
    for education in user_educations:
        for edu_media in education.medias:
            user_documents.append(edu_media.id)

    user_dict["media_education_ids"] = user_documents
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
    user_dict = user.to_dict()
    return user_dict
