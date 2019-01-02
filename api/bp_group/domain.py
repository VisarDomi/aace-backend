from . import backend

from ..common.models import Group
from ..common.models import User

def return_group(group):
    users = group.users.all()
    group = group.to_dict()
    users = {x.id: x.to_dict() for x in users}
    return_object = {
                        "group_data" : {**group},
                        "users" : {**users}
                    }
    return return_object

def create_group(group_data):
    """Create group.
    :param group_data: group information
    :type group_data: dict
    :returns: serialized group object
    :rtype: dict
    """
    group = backend.create_group(group_data)
    group = return_group(group)
    return group

def get_group(group_id):
    """Get Group by id.
    :param group_id: id of the group to be retrived
    :type group_id: integer
    :returns: serialized Group object
    :rtype: dict
    """
    group = backend.get_group(group_id)
    group = return_group(group)
    return group

def get_all_groups():
    """Get all groups.
    :returns: serialized Group objects
    :rtype: list
    """
    groups = backend.get_all_groups()
    return [
        group.to_dict() for group in groups
    ]


def update_group(group_data, group_id):
    """Update Group.
    :param group_data: Group information
    :type group_data: dict
    :param group_id: id of the Group to be updated
    :type group_id: integer
    :returns: serialized Group object
    :rtype: dict
    """
    group = backend.update_group(group_data, group_id)
    group = return_group(group)
    return group


def delete_group(group_id):
    """Delete Group.
    :param group_id: id of the Group to be deleted
    :type group_id: integer
    """
    backend.delete_group(group_id)

def add_user_to_group(group_data, group_id):
    group = backend.add_user_to_group(group_data, group_id)
    group = return_group(group)
    return group

def remove_user_from_group(group_data, group_id):
    group = backend.remove_user_from_group(group_data, group_id)
    group = return_group(group)
    return group



