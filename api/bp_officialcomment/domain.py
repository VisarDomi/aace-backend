from . import backend
from ..helper_functions.get_by_id import (
    get_officialcomment_by_id as backend_get_officialcomment_by_id,
)
from ..helper_functions.constants import ONLY


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

    # author
    officialcomment_dict["author"] = officialcomment.author.to_dict(only=ONLY)
    officialcomment_dict[
        "author_organizationgroup"
    ] = officialcomment.author.organizationgroup.name

    # medias
    officialcomment_medias = []
    for officialcomment_media in officialcomment.medias:
        officialcomment_medias.append(officialcomment_media.to_dict())
    officialcomment_dict["officialcomment_medias"] = officialcomment_medias

    return officialcomment_dict


def get_all_officialcomments(officialcommunication_id):
    officialcomments = backend.get_all_officialcomments(officialcommunication_id)
    officialcomments_list = []
    for officialcomment in officialcomments:
        officialcomment_dict = officialcomment.to_dict()

        # author
        officialcomment_dict["author"] = officialcomment.author.to_dict(only=ONLY)
        officialcomment_dict[
            "author_organizationgroup"
        ] = officialcomment.author.organizationgroup.name

        # medias
        officialcomment_medias = []
        for officialcomment_media in officialcomment.medias:
            officialcomment_medias.append(officialcomment_media.to_dict())
        officialcomment_dict["officialcomment_medias"] = officialcomment_medias

        officialcomments_list += [officialcomment_dict]

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
