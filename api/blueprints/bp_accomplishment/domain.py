from . import backend
import json


def create_accomplishment(accomplishment_data, user_id):
    accomplishment = backend.create_accomplishment(accomplishment_data, user_id)
    return accomplishment.to_json(max_nesting=1)


def get_accomplishment_by_id(accomplishment_id):
    accomplishment = backend.get_accomplishment_by_id(accomplishment_id)
    accomplishment_json = accomplishment.to_json(max_nesting=1)
    return accomplishment_json


def get_all_accomplishments(user_id):
    accomplishments = backend.get_all_accomplishments(user_id)
    list_of_accomplishments = [
        accomplishment.to_dict(max_nesting=1) for accomplishment in accomplishments
    ]
    json_dump_of_list_of_accomplishments = json.dumps(
        list_of_accomplishments, default=str
    )
    return json_dump_of_list_of_accomplishments


def update_accomplishment(accomplishment_data, user_id, accomplishment_id):
    accomplishment = backend.update_accomplishment(
        accomplishment_data, user_id, accomplishment_id
    )
    return accomplishment.to_json(max_nesting=1)


def delete_accomplishment(user_id, accomplishment_id):
    backend.delete_accomplishment(user_id, accomplishment_id)
