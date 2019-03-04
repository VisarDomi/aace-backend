from . import backend


def create_user(user_data):
    user = backend.create_user(user_data)
    EXCLUDE = ["password_hash"]
    user_dict = user.to_dict(exclude=EXCLUDE)

    return user_dict


def get_user_by_id(user_id):
    user = backend.get_user_by_id(user_id)
    ONLY = [
        "register_status",
        "id",
        "first_name",
        "last_name",
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

    user_documents = []
    user_educations = user.educations.all()
    for education in user_educations:
        for edu_media in education.medias:
            user_documents.append(edu_media.id)

    user_dict["document_ids"] = user_documents
    user_dict["years_of_experience"] = "5"

    return user_dict


def get_all_users():
    users = backend.get_all_users()
    ONLY = [
        "register_status",
        "id",
        "first_name",
        "last_name",
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

    # users_list = [
    #     user_dict = user.to_dict(only=ONLY)
    #     for user in users
    # ]

    users_list = []
    for user in users:
        user_dict = user.to_dict(only=ONLY)
        user_dict["years_of_experience"] = "6"
        users_list.append(user_dict)

    return users_list


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    ONLY = [
        "id",
        "first_name",
        "last_name",
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


def delete_user(user_id):
    backend.delete_user(user_id)
