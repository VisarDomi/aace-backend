from flask import g
from ..common.exceptions import CannotChangeOthersComment
from ..models.items import Comment
from ..bp_media_comment.backend import get_all_medias, delete_media
from ..helper_functions.get_by_id import (
    get_comment_by_id,
    get_communication_by_id,
)


def create_comment(comment_data, communication_id):
    comment = Comment(**comment_data)
    comment.communication = get_communication_by_id(
        communication_id
    )
    comment.author = g.current_user
    comment.save()

    return comment


def get_all_comments(communication_id):
    communication = get_communication_by_id(communication_id)
    for group in communication.organizationgroups.all():
        if g.current_user in group.users.all() or g.current_user.role == "admin":
            comments = communication.comments.all()

    return comments


def same_user(communication_id, comment_id):
    is_same_user = False
    communication = get_communication_by_id(communication_id)
    for group in communication.organizationgroups.all():
        if g.current_user in group.users.all():
            comment = get_comment_by_id(
                communication_id, comment_id
            )
            if g.current_user == comment.author:
                is_same_user = True

    return is_same_user


def update_comment(
    comment_data, communication_id, comment_id
):
    if same_user(communication_id, comment_id):
        comment = get_comment_by_id(
            communication_id, comment_id
        )
        comment.update(**comment_data)
        comment.save()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)

    return comment


def delete_comment(communication_id, comment_id):
    if same_user(communication_id, comment_id):
        for media in get_all_medias(communication_id, comment_id):
            delete_media(communication_id, comment_id, media.id)
        comment = get_comment_by_id(
            communication_id, comment_id
        )
        comment.delete()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)
