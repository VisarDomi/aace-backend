from . import backend
import json


def create_group(group_data):
    group = backend.create_group(group_data)

    return group.to_json(max_nesting=1)


def get_group_by_id(group_id):
    group = backend.get_group_by_id(group_id)
    group_json = group.to_json(max_nesting=1)

    return group_json


def get_all_groups():
    groups = backend.get_all_groups()
    list_of_groups = [
        group.to_dict(max_nesting=1) for group in groups
    ]

    return json.dumps(list_of_groups, default=str)


def update_group(group_data, group_id):
    group = backend.update_group(group_data, group_id)

    return group.to_json(max_nesting=1)


def delete_group(group_id):
    backend.delete_group(group_id)


def add_user_to_group(group_id, user_id):
    group = backend.add_user_to_group(group_id, user_id)

    return group.to_json(max_nesting=1)


def remove_user_from_group(group_id, user_id):
    backend.remove_user_from_group(group_id, user_id)
