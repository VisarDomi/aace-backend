from flask import g
from ..common.exceptions import CannotChangeOthersComment
from ..common.models import OfficialComment, OfficialCommunication
from ..bp_media_officialcomment.backend import get_all_medias, delete_media
from ..helper_functions.get_by_id import (
    get_officialcomment_by_id,
    get_officialcommunication_by_id,
)


def create_officialcomment(officialcomment_data, officialcommunication_id):
    officialcomment = OfficialComment(**officialcomment_data)
    officialcomment.officialcommunication = get_officialcommunication_by_id(
        officialcommunication_id
    )
    officialcomment.author = g.current_user
    officialcomment.save()

    return officialcomment


def get_all_officialcomments(officialcommunication_id):
    officialcomments = OfficialComment.query.filter(
        OfficialCommunication.id == officialcommunication_id
    ).all()
    allowed_officialcomments = []
    if g.current_user.role == "admin":
        allowed_officialcomments = officialcomments
    else:
        communication = get_officialcommunication_by_id(officialcommunication_id)
        for group in communication.organizationgroups.all():
            if g.current_user in group.users.all():
                for comment in officialcomments:
                    allowed_officialcomments.append(comment)

    return allowed_officialcomments


def same_user(officialcommunication_id, officialcomment_id):
    is_same_user = False
    communication = get_officialcommunication_by_id(officialcommunication_id)
    for group in communication.organizationgroups.all():
        if g.current_user in group.users.all():
            comment = get_officialcomment_by_id(
                officialcommunication_id, officialcomment_id
            )
            if g.current_user == comment.author:
                is_same_user = True

    return is_same_user


def update_officialcomment(
    officialcomment_data, officialcommunication_id, officialcomment_id
):
    if same_user(officialcommunication_id, officialcomment_id):
        officialcomment = get_officialcomment_by_id(
            officialcommunication_id, officialcomment_id
        )
        officialcomment.update(**officialcomment_data)
        officialcomment.save()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)

    return officialcomment


def delete_officialcomment(officialcommunication_id, officialcomment_id):
    if same_user(officialcommunication_id, officialcomment_id):
        for media in get_all_medias(officialcommunication_id, officialcomment_id):
            delete_media(officialcommunication_id, officialcomment_id, media.id)
        officialcomment = get_officialcomment_by_id(
            officialcommunication_id, officialcomment_id
        )
        officialcomment.delete()
    else:
        msg = f"You can't change other people's comment."
        raise CannotChangeOthersComment(message=msg)
