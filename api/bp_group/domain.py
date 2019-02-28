from . import backend


def create_group(group_data):
    group = backend.create_group(group_data)
    group_dict = group.to_dict()

    return group_dict


def get_group_by_id(group_id):
    group = backend.get_group_by_id(group_id)
    group_dict = group.to_dict()

    return group_dict


def get_all_groups():
    groups = backend.get_all_groups()
    groups_list = [group.to_dict() for group in groups]

    return groups_list


def update_group(group_data, group_id):
    group = backend.update_group(group_data, group_id)
    group_dict = group.to_dict()

    return group_dict


def delete_group(group_id):
    backend.delete_group(group_id)


def add_user_to_group(group_id, user_id):
    group = backend.add_user_to_group(group_id, user_id)
    group_dict = group.to_dict()

    return group_dict


def remove_user_from_group(group_id, user_id):
    backend.remove_user_from_group(group_id, user_id)
