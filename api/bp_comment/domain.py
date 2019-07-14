from . import backend
from ..helper_functions.get_by_id import (
    get_comment_by_id as backend_get_comment_by_id,
)
from ..helper_functions.constants import ONLY


def create_comment(comment_data, communication_id):
    comment = backend.create_comment(
        comment_data, communication_id
    )
    comment_dict = comment.to_dict()

    return comment_dict


def get_comment_by_id(communication_id, comment_id):
    comment = backend_get_comment_by_id(
        communication_id, comment_id
    )
    comment_dict = comment.to_dict()

    # author
    comment_dict["author"] = comment.author.to_dict(only=ONLY)
    comment_dict[
        "author_organizationgroup"
    ] = comment.author.organizationgroup.name

    # medias
    comment_medias = []
    for comment_media in comment.medias:
        comment_medias.append(comment_media.to_dict())
    comment_dict["comment_medias"] = comment_medias

    return comment_dict


def get_all_comments(communication_id):
    comments = backend.get_all_comments(communication_id)
    comments_list = []
    for comment in comments:
        comment_dict = comment.to_dict()

        # author
        comment_dict["author"] = comment.author.to_dict(only=ONLY)
        comment_dict[
            "author_organizationgroup"
        ] = comment.author.organizationgroup.name

        # medias
        comment_medias = []
        for comment_media in comment.medias:
            comment_medias.append(comment_media.to_dict())
        comment_dict["comment_medias"] = comment_medias

        comments_list += [comment_dict]

    return comments_list


def update_comment(
    comment_data, communication_id, comment_id
):
    comment = backend.update_comment(
        comment_data, communication_id, comment_id
    )
    comment_dict = comment.to_dict()

    return comment_dict


def delete_comment(communication_id, comment_id):
    backend.delete_comment(communication_id, comment_id)
