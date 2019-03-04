from . import backend


def search_users(search_user_data):
    users = backend.search_users(search_user_data)
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
    users_list = [user.to_dict(only=ONLY) for user in users]

    return users_list
