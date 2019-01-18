from . import backend
import json


def create_media(media_data, user_id, experience_id):
    media = backend.create_media(media_data, user_id, experience_id)
    return media.to_json(max_nesting=2)


def get_media_by_id(media_id):
    media = backend.get_media_by_id(media_id)
    media_json = media.to_json(max_nesting=2)
    return media_json


def get_all_medias():
    medias = backend.get_all_medias()
    list_of_medias = [
        media.to_dict(max_nesting=2) for media in medias
    ]
    json_dump_of_list_of_medias = json.dumps(list_of_medias, default=str)
    return json_dump_of_list_of_medias


def update_media(media_data, user_id, media_id):
    media = backend.update_media(media_data, user_id, media_id)
    return media.to_json(max_nesting=2)


def delete_media(media_id):
    backend.delete_media(media_id)
