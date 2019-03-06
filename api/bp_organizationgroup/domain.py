from . import backend


def create_organizationgroup(organizationgroup_data):
    organizationgroup = backend.create_organizationgroup(organizationgroup_data)
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def get_organizationgroup_by_id(organizationgroup_id):
    organizationgroup = backend.get_organizationgroup_by_id(organizationgroup_id)
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def get_all_organizationgroups():
    organizationgroups = backend.get_all_organizationgroups()
    organizationgroups_list = [
        organizationgroup.to_dict() for organizationgroup in organizationgroups
    ]

    return organizationgroups_list


def update_organizationgroup(organizationgroup_data, organizationgroup_id):
    organizationgroup = backend.update_organizationgroup(
        organizationgroup_data, organizationgroup_id
    )
    organizationgroup_dict = organizationgroup.to_dict()

    return organizationgroup_dict


def delete_organizationgroup(organizationgroup_id):
    backend.delete_organizationgroup(organizationgroup_id)
