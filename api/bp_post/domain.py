from . import backend
import json


def create_post(post_data, user_id):
    post = backend.create_post(post_data, user_id)
    return post.to_json(max_nesting=2)


def get_post_by_id(post_id):
    post = backend.get_post_by_id(post_id)
    post_json = post.to_json(max_nesting=2)
    return post_json


def get_all_posts(user_id):
    posts = backend.get_all_posts(user_id)
    list_of_posts = [
        post.to_dict(max_nesting=2) for post in posts
    ]
    json_dump_of_list_of_posts = json.dumps(list_of_posts, default=str)
    return json_dump_of_list_of_posts


def update_post(post_data, user_id, post_id):
    post = backend.update_post(post_data, user_id, post_id)
    return post.to_json(max_nesting=2)


def delete_post(post_id):
    backend.delete_post(post_id)
