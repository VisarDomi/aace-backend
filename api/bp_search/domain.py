from . import backend
from ..helper_functions.constants import ONLY


def search_users(search_user_data):
    users = backend.search_users(search_user_data)
    users_list = []
    for user in users:
        user_dict = user.to_dict(only=ONLY)
        user_dict["years_of_experience"] = "6"
        users_list.append(user_dict)

    return users_list
