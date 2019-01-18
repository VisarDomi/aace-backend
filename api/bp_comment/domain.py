from . import backend
import json


def create_comment(comment_data):
    comment = backend.create_comment(comment_data)
    return comment.to_json(max_nesting=2)


def get_comment_by_id(comment_id):
    comment = backend.get_comment_by_id(comment_id)
    comment_json = comment.to_json(max_nesting=2)
    return comment_json


def get_all_comments():
    comments = backend.get_all_comments()
    list_of_comments = [
        comment.to_dict(max_nesting=2) for comment in comments
    ]
    json_dump_of_list_of_comments = json.dumps(list_of_comments, default=str)
    return json_dump_of_list_of_comments


def update_comment(comment_data, comment_id):
    comment = backend.update_comment(comment_data, comment_id)
    return comment.to_json(max_nesting=2)


def delete_comment(comment_id):
    backend.delete_comment(comment_id)
