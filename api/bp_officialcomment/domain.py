from . import backend
from ..helper_functions.get_by_id import (
    get_officialcomment_by_id as backend_get_officialcomment_by_id,
)


def create_officialcomment(officialcomment_data, officialcommunication_id):
    officialcomment = backend.create_officialcomment(
        officialcomment_data, officialcommunication_id
    )
    officialcomment_dict = officialcomment.to_dict()

    return officialcomment_dict


def get_officialcomment_by_id(officialcommunication_id, officialcomment_id):
    officialcomment = backend_get_officialcomment_by_id(
        officialcommunication_id, officialcomment_id
    )
    officialcomment_dict = officialcomment.to_dict()

    media_officialcomment_ids = []
    for officialcomment_media in officialcomment.medias:
        media_officialcomment_ids.append(officialcomment_media.id)
    officialcomment_dict["media_officialcomment_ids"] = media_officialcomment_ids

    return officialcomment_dict


def get_all_officialcomments(officialcommunication_id):
    officialcomments = backend.get_all_officialcomments(officialcommunication_id)
    officialcomments_list = [
        officialcomment.to_dict() for officialcomment in officialcomments
    ]

    return officialcomments_list


def update_officialcomment(
    officialcomment_data, officialcommunication_id, officialcomment_id
):
    officialcomment = backend.update_officialcomment(
        officialcomment_data, officialcommunication_id, officialcomment_id
    )
    officialcomment_dict = officialcomment.to_dict()

    return officialcomment_dict


def delete_officialcomment(officialcommunication_id, officialcomment_id):
    backend.delete_officialcomment(officialcommunication_id, officialcomment_id)
