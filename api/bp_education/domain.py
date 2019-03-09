from . import backend
from ..helper_functions.get_by_id import (
    get_education_by_id as backend_get_education_by_id,
)


def create_education(education_data, user_id):
    education = backend.create_education(education_data, user_id)
    education_dict = education.to_dict()

    return education_dict


def get_education_by_id(education_id):
    education = backend_get_education_by_id(education_id)
    education_dict = education.to_dict()

    return education_dict


def get_all_educations(user_id):
    educations = backend.get_all_educations(user_id)
    educations_list = [education.to_dict() for education in educations]

    return educations_list


def update_education(education_data, user_id, education_id):
    education = backend.update_education(education_data, user_id, education_id)
    education_dict = education.to_dict()

    return education_dict


def delete_education(user_id, education_id):
    backend.delete_education(user_id, education_id)
