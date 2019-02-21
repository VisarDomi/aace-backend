from . import backend
import json


def create_education(education_data, user_id):
    education = backend.create_education(education_data, user_id)
    return education.to_json(max_nesting=1)


def get_education_by_id(education_id):
    education = backend.get_education_by_id(education_id)
    education_json = education.to_json(max_nesting=1)
    return education_json


def get_all_educations(user_id):
    educations = backend.get_all_educations(user_id)
    list_of_educations = [
        education.to_dict(max_nesting=1) for education in educations
    ]
    json_dump_of_list_of_educations = json.dumps(list_of_educations, default=str)
    return json_dump_of_list_of_educations


def update_education(education_data, user_id, education_id):
    education = backend.update_education(education_data, user_id, education_id)
    return education.to_json(max_nesting=1)


def delete_education(user_id, education_id):
    backend.delete_education(user_id, education_id)
