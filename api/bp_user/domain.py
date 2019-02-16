from . import backend
import json


def create_user(user_data):
    user = backend.create_user(user_data)
    return user.to_json(max_nesting=1)


def get_user_by_id(user_id):
    user = backend.get_user_by_id(user_id)
    user_json = user.to_json(max_nesting=1)
    return user_json


def get_all_users():
    users = backend.get_all_users()

    # list_of_users = [
    #     user.to_dict() for user in users
    # ]
    # json_dump_of_list_of_users = json.dumps(list_of_users, default=str)
    list_of_users_flusk = [
        user.to_dict_flusk(only=["id", "first_name", "last_name"]) for user in users
    ]
    json_dump_of_list_of_users = json.dumps(list_of_users_flusk, default=str)
    return json_dump_of_list_of_users


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    return user.to_json(max_nesting=1)


def delete_user(user_id):
    backend.delete_user(user_id)
