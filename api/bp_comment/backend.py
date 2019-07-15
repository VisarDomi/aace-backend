from flask import g
from ..common.exceptions import CannotChangeOthersComment
from ..models.items import Comment
from ..bp_media_comment.backend import get_medias, delete_media
from ..helper_functions.get_by_id import (
    get_comment_by_id,
    get_communication_by_id,
    get_event_by_id,
    get_poll_by_id,
)


def create_communication_comment(comment_data, communication_id):
    comment = Comment(**comment_data)
    comment.communication = get_communication_by_id(communication_id)
    comment.author = g.current_user
    comment.save()

    return comment


def get_communication_comments(communication_id):
    communication = get_communication_by_id(communication_id)
    comments = []
    for group in communication.organizationgroups.all():
        if g.current_user in group.users.all():
            comments = communication.comments.all()
    if g.current_user.role == "admin":
        comments = communication.comments.all()

    return comments


def same_communication_user(communication_id, comment_id):
    is_same_user = False
    communication = get_communication_by_id(communication_id)
    for group in communication.organizationgroups.all():
        if g.current_user in group.users.all():
            comment = get_comment_by_id(comment_id)
            if g.current_user == comment.author:
                is_same_user = True

    return is_same_user


def update_communication_comment(comment_data, communication_id, comment_id):
    if same_communication_user(communication_id, comment_id):
        comment = get_comment_by_id(comment_id)
        comment.update(**comment_data)
        comment.save()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)

    return comment


def delete_communication_comment(communication_id, comment_id):
    if same_communication_user(communication_id, comment_id):
        for media in get_medias(comment_id):
            delete_media(comment_id, media.id)
        comment = get_comment_by_id(comment_id)
        comment.delete()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)


def create_event_comment(comment_data, event_id):
    comment = Comment(**comment_data)
    comment.event = get_event_by_id(event_id)
    comment.author = g.current_user
    comment.save()

    return comment


def get_event_comments(event_id):
    event = get_event_by_id(event_id)
    comments = []
    for group in event.organizationgroups.all():
        if g.current_user in group.users.all():
            comments = event.comments.all()
    if g.current_user.role == "admin":
        comments = event.comments.all()
    for group in event.organizationgroups.all():
        if g.current_user in group.users.all() or g.current_user.role == "admin":
            comments = event.comments.all()

    return comments


def same_event_user(event_id, comment_id):
    is_same_user = False
    event = get_event_by_id(event_id)
    for group in event.organizationgroups.all():
        if g.current_user in group.users.all():
            comment = get_comment_by_id(comment_id)
            if g.current_user == comment.author:
                is_same_user = True

    return is_same_user


def update_event_comment(comment_data, event_id, comment_id):
    if same_event_user(event_id, comment_id):
        comment = get_comment_by_id(comment_id)
        comment.update(**comment_data)
        comment.save()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)

    return comment


def delete_event_comment(event_id, comment_id):
    if same_event_user(event_id, comment_id):
        for media in get_medias(comment_id):
            delete_media(comment_id, media.id)
        comment = get_comment_by_id(comment_id)
        comment.delete()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)


def create_poll_comment(comment_data, poll_id):
    comment = Comment(**comment_data)
    comment.poll = get_poll_by_id(poll_id)
    comment.author = g.current_user
    comment.save()

    return comment


def get_poll_comments(poll_id):
    poll = get_poll_by_id(poll_id)
    comments = []
    for group in poll.organizationgroups.all():
        if g.current_user in group.users.all():
            comments = poll.comments.all()
    if g.current_user.role == "admin":
        comments = poll.comments.all()
    for group in poll.organizationgroups.all():
        if g.current_user in group.users.all() or g.current_user.role == "admin":
            comments = poll.comments.all()

    return comments


def same_poll_user(poll_id, comment_id):
    is_same_user = False
    poll = get_poll_by_id(poll_id)
    for group in poll.organizationgroups.all():
        if g.current_user in group.users.all():
            comment = get_comment_by_id(comment_id)
            if g.current_user == comment.author:
                is_same_user = True

    return is_same_user


def update_poll_comment(comment_data, poll_id, comment_id):
    if same_poll_user(poll_id, comment_id):
        comment = get_comment_by_id(comment_id)
        comment.update(**comment_data)
        comment.save()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)

    return comment


def delete_poll_comment(poll_id, comment_id):
    if same_poll_user(poll_id, comment_id):
        for media in get_medias(comment_id):
            delete_media(comment_id, media.id)
        comment = get_comment_by_id(comment_id)
        comment.delete()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)
