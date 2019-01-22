from . import backend
import json


def create_media(
    media_data, user_id, comment_id, event_id, experience_id, message_id, post_id
):
    medias = backend.create_media(
        media_data, user_id, comment_id, event_id, experience_id, message_id, post_id
    )
    list_of_medias = [media.to_dict(max_nesting=2) for media in medias]
    json_dump_of_list_of_medias = json.dumps(list_of_medias, default=str)
    return json_dump_of_list_of_medias


def get_media_by_id(media_id):
    media = backend.get_media_by_id(media_id)
    media_json = media.to_json(max_nesting=2)
    return media_json


def get_all_medias(comment_id, event_id, experience_id, message_id, post_id):
    medias = backend.get_all_medias(
        comment_id, event_id, experience_id, message_id, post_id
    )
    list_of_medias = [media.to_dict(max_nesting=2) for media in medias]
    json_dump_of_list_of_medias = json.dumps(list_of_medias, default=str)
    return json_dump_of_list_of_medias


def update_media(media_data, user_id, media_id):
    media = backend.update_media(media_data, user_id, media_id)
    return media.to_json(max_nesting=2)


def delete_media(user_id, media_id):
    backend.delete_media(user_id, media_id)
