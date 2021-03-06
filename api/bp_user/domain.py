from . import backend
from ..helper_functions.get_by_id import get_user_by_id
from ..helper_functions.constants import ONLY


def create_user(user_data):
    user = backend.create_user(user_data)
    EXCLUDE = ["password_hash"]
    user_dict = user.to_dict(exclude=EXCLUDE)

    return user_dict


def get_users():
    users = backend.get_users()
    users_list = []
    for user in users:
        user_dict = user.to_dict(only=ONLY)
        user_dict["years_of_experience"] = "6"
        users_list.append(user_dict)

    return users_list


def get_users_count():
    count = backend.get_users_count()
    count_dict = {"total_members": count}

    return count_dict


def get_user(user_id):
    user = get_user_by_id(user_id)
    user_dict = user.to_dict(only=ONLY)
    user_dict["years_of_experience"] = "6"

    return user_dict


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    user_dict = user.to_dict(only=ONLY)

    return user_dict


def delete_user(user_id):
    backend.delete_user(user_id)
