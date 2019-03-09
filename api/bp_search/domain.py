from . import backend


def search_users(search_user_data):
    users = backend.search_users(search_user_data)
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
    # users_list = [user.to_dict(only=ONLY) for user in users]

    users_list = []
    for user in users:
        user_dict = user.to_dict(only=ONLY)
        user_dict["years_of_experience"] = "6"
        users_list.append(user_dict)

    return users_list
