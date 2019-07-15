from . import backend
from ..helper_functions.get_by_id import get_communication_by_id


def create_communication(communication_data):
    communication = backend.create_communication(communication_data)
    communication_dict = communication.to_dict()

    return communication_dict


def get_communications():
    communications = backend.get_communications()
    communications_list = [communication.to_dict() for communication in communications]

    return communications_list


def get_communication(communication_id):
    communication = get_communication_by_id(communication_id)
    communication_dict = communication.to_dict()

    communication_medias = []
    for communication_media in communication.medias:
        communication_medias.append(communication_media.to_dict())
    communication_dict["communication_medias"] = communication_medias

    return communication_dict


def update_communication(communication_data, communication_id):
    communication = backend.update_communication(communication_data, communication_id)
    communication_dict = communication.to_dict()

    return communication_dict


def delete_communication(communication_id):
    backend.delete_communication(communication_id)


def get_organizationgroups_from_communication(communication_id):
    organizationgroups = backend.get_organizationgroups_from_communication(
        communication_id
    )

    organizationgroups_list = [
        organizationgroup.to_dict() for organizationgroup in organizationgroups
    ]

    return organizationgroups_list


def add_organizationgroup_to_communication(communication_id, organizationgroup_id):
    communication = backend.add_organizationgroup_to_communication(
        communication_id, organizationgroup_id
    )
    communication_dict = communication.to_dict()

    return communication_dict


def remove_organizationgroup_from_communication(communication_id, organizationgroup_id):
    backend.remove_organizationgroup_from_communication(
        communication_id, organizationgroup_id
    )


def send_email(communication_id):
    backend.send_email(communication_id)
