from . import backend
import json
from flask import jsonify


def get_user_by_id(user_id):
    user = backend.get_user_by_id(user_id)
    user_json = user.to_json(max_nesting=1)
    return user_json


def get_applying_users():
    users = backend.get_applying_users()
    list_of_users = [user.to_dict(max_nesting=1) for user in users]
    json_dump_of_list_of_users = json.dumps(list_of_users, default=str)
    return json_dump_of_list_of_users


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    # user_json = user.to_json(max_nesting=1)
    # return user_json
    user_dict_flusk = user.to_dict_flusk()
    return jsonify(user_dict_flusk)


def delete_user(user_id):
    backend.delete_user(user_id)


def download(media_id):
    return backend.download(media_id)
