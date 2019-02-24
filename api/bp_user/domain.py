from . import backend
import json
from flask import jsonify


def create_user(user_data):
    user = backend.create_user(user_data)
    # user_json = user.to_json(max_nesting=1)
    # return user_json
    EXCLUDE = ["password_hash"]
    user_dict_flusk = user.to_dict_flusk(exclude=EXCLUDE)
    return jsonify(user_dict_flusk)


def get_user_by_id(user_id):
    user = backend.get_user_by_id(user_id)

    # user_json = user.to_json(max_nesting=3)
    # return user_json

    ONLY = [
        "profile_picture",
        "register_status",
        "token",
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
    user_dict_flusk = user.to_dict_flusk(only=ONLY)

    user_documents = []
    user_educations = user.educations.all()
    for education in user_educations:
        for edu_media in education.medias:
            user_documents.append(edu_media.id)

    user_dict_flusk["document_ids"] = user_documents
    user_dict_flusk["years_of_experience"] = '5'
    print("user_dict_flusk['document_ids'] :", user_dict_flusk["document_ids"])
    return jsonify(user_dict_flusk)


def get_all_users():
    users = backend.get_all_users()
    
    ####-------SQLAthanor-----------####
    # list_of_users = [
    #     user.to_dict(max_nesting=3) for user in users
    # ]
    # json_dump_of_list_of_users = json.dumps(list_of_users, default=str)

    ####-------Flusk-----------####
    ONLY = [
        "profile_picture",
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

    # list_of_users_flusk = [
    #     user_dict_flusk = user.to_dict_flusk(only=ONLY)
    #     for user in users
    # ]
    list_of_users_flusk = []
    for user in users:
        user_dict_flusk = user.to_dict_flusk(only=ONLY)
        user_dict_flusk["years_of_experience"] = '6'
        list_of_users_flusk.append(user_dict_flusk)


    json_dump_of_list_of_users_flusk = json.dumps(list_of_users_flusk, default=str)
    return json_dump_of_list_of_users_flusk


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    # user_json = user.to_json(max_nesting=1)
    # return user_json
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
    user_dict_flusk = user.to_dict_flusk(only=ONLY)
    return jsonify(user_dict_flusk)


def delete_user(user_id):
    backend.delete_user(user_id)
