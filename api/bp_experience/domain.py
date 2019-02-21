from . import backend
import json


def create_experience(experience_data, user_id):
    experience = backend.create_experience(experience_data, user_id)
    return experience.to_json(max_nesting=1)


def get_experience_by_id(experience_id):
    experience = backend.get_experience_by_id(experience_id)
    experience_json = experience.to_json(max_nesting=1)
    return experience_json


def get_all_experiences(user_id):
    experiences = backend.get_all_experiences(user_id)
    list_of_experiences = [
        experience.to_dict(max_nesting=1) for experience in experiences
    ]
    json_dump_of_list_of_experiences = json.dumps(list_of_experiences, default=str)
    return json_dump_of_list_of_experiences


def update_experience(experience_data, user_id, experience_id):
    experience = backend.update_experience(experience_data, user_id, experience_id)
    return experience.to_json(max_nesting=1)


def delete_experience(user_id, experience_id):
    backend.delete_experience(user_id, experience_id)
