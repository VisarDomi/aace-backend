from . import backend


def create_officialcommunication(officialcommunication_data):
    officialcommunication = backend.create_officialcommunication(
        officialcommunication_data
    )
    officialcommunication_dict = officialcommunication.to_dict()

    return officialcommunication_dict


def get_officialcommunication_by_id(officialcommunication_id):
    officialcommunication = backend.get_officialcommunication_by_id(
        officialcommunication_id
    )
    officialcommunication_dict = officialcommunication.to_dict()

    return officialcommunication_dict


def get_all_officialcommunications():
    officialcommunications = backend.get_all_officialcommunications()
    officialcommunications_list = [
        officialcommunication.to_dict()
        for officialcommunication in officialcommunications
    ]

    return officialcommunications_list


def update_officialcommunication(officialcommunication_data, officialcommunication_id):
    officialcommunication = backend.update_officialcommunication(
        officialcommunication_data, officialcommunication_id
    )
    officialcommunication_dict = officialcommunication.to_dict()

    return officialcommunication_dict


def delete_officialcommunication(officialcommunication_id):
    backend.delete_officialcommunication(officialcommunication_id)


def get_organizationgroups_from_officialcommunication(officialcommunication_id):
    organizationgroups = backend.get_organizationgroups_from_officialcommunication(
        officialcommunication_id
    )

    organizationgroups_list = [
        organizationgroup.to_dict() for organizationgroup in organizationgroups
    ]

    return organizationgroups_list


def add_organizationgroup_to_officialcommunication(
    officialcommunication_id, organizationgroup_id
):
    officialcommunication = backend.add_organizationgroup_to_officialcommunication(
        officialcommunication_id, organizationgroup_id
    )
    officialcommunication_dict = officialcommunication.to_dict()

    return officialcommunication_dict


def remove_organizationgroup_from_officialcommunication(
    officialcommunication_id, organizationgroup_id
):
    backend.remove_organizationgroup_from_officialcommunication(
        officialcommunication_id, organizationgroup_id
    )
