from . import backend
from ..helper_functions.get_by_id import get_comment_by_id
from ..helper_functions.constants import ONLY


def create_communication_comment(comment_data, communication_id):
    comment = backend.create_communication_comment(comment_data, communication_id)
    comment_dict = comment.to_dict()

    return comment_dict


def get_communication_comments(communication_id):
    comments = backend.get_communication_comments(communication_id)
    comments_list = []
    for comment in comments:
        comment_dict = comment.to_dict()

        # author
        comment_dict["author"] = comment.author.to_dict(only=ONLY)
        comment_dict["author_organizationgroup"] = comment.author.organizationgroup.name

        # medias
        comment_medias = []
        for comment_media in comment.medias:
            comment_medias.append(comment_media.to_dict())
        comment_dict["comment_medias"] = comment_medias

        comments_list += [comment_dict]

    return comments_list


def get_communication_comment(communication_id, comment_id):
    comment = get_comment_by_id(comment_id)
    comment_dict = comment.to_dict()

    # author
    comment_dict["author"] = comment.author.to_dict(only=ONLY)
    comment_dict["author_organizationgroup"] = comment.author.organizationgroup.name

    # medias
    comment_medias = []
    for comment_media in comment.medias:
        comment_medias.append(comment_media.to_dict())
    comment_dict["comment_medias"] = comment_medias

    return comment_dict


def update_communication_comment(comment_data, communication_id, comment_id):
    comment = backend.update_communication_comment(
        comment_data, communication_id, comment_id
    )
    comment_dict = comment.to_dict()

    return comment_dict


def delete_communication_comment(communication_id, comment_id):
    backend.delete_communication_comment(communication_id, comment_id)


def create_event_comment(comment_data, event_id):
    comment = backend.create_event_comment(comment_data, event_id)
    comment_dict = comment.to_dict()

    return comment_dict


def get_event_comments(event_id):
    comments = backend.get_event_comments(event_id)
    comments_list = []
    for comment in comments:
        comment_dict = comment.to_dict()

        # author
        comment_dict["author"] = comment.author.to_dict(only=ONLY)
        comment_dict["author_organizationgroup"] = comment.author.organizationgroup.name

        # medias
        comment_medias = []
        for comment_media in comment.medias:
            comment_medias.append(comment_media.to_dict())
        comment_dict["comment_medias"] = comment_medias

        comments_list += [comment_dict]

    return comments_list


def get_event_comment(event_id, comment_id):
    comment = get_comment_by_id(comment_id)
    comment_dict = comment.to_dict()

    # author
    comment_dict["author"] = comment.author.to_dict(only=ONLY)
    comment_dict["author_organizationgroup"] = comment.author.organizationgroup.name

    # medias
    comment_medias = []
    for comment_media in comment.medias:
        comment_medias.append(comment_media.to_dict())
    comment_dict["comment_medias"] = comment_medias

    return comment_dict


def update_event_comment(comment_data, event_id, comment_id):
    comment = backend.update_event_comment(comment_data, event_id, comment_id)
    comment_dict = comment.to_dict()

    return comment_dict


def delete_event_comment(event_id, comment_id):
    backend.delete_event_comment(event_id, comment_id)


def create_poll_comment(comment_data, poll_id):
    comment = backend.create_poll_comment(comment_data, poll_id)
    comment_dict = comment.to_dict()

    return comment_dict


def get_poll_comments(poll_id):
    comments = backend.get_poll_comments(poll_id)
    comments_list = []
    for comment in comments:
        comment_dict = comment.to_dict()

        # author
        comment_dict["author"] = comment.author.to_dict(only=ONLY)
        comment_dict["author_organizationgroup"] = comment.author.organizationgroup.name

        # medias
        comment_medias = []
        for comment_media in comment.medias:
            comment_medias.append(comment_media.to_dict())
        comment_dict["comment_medias"] = comment_medias

        comments_list += [comment_dict]

    return comments_list


def get_poll_comment(poll_id, comment_id):
    comment = get_comment_by_id(comment_id)
    comment_dict = comment.to_dict()

    # author
    comment_dict["author"] = comment.author.to_dict(only=ONLY)
    comment_dict["author_organizationgroup"] = comment.author.organizationgroup.name

    # medias
    comment_medias = []
    for comment_media in comment.medias:
        comment_medias.append(comment_media.to_dict())
    comment_dict["comment_medias"] = comment_medias

    return comment_dict


def update_poll_comment(comment_data, poll_id, comment_id):
    comment = backend.update_poll_comment(comment_data, poll_id, comment_id)
    comment_dict = comment.to_dict()

    return comment_dict


def delete_poll_comment(poll_id, comment_id):
    backend.delete_poll_comment(poll_id, comment_id)
