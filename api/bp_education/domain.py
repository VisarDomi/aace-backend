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

    # medias
    media_education_ids = []
    for education_media in education.medias:
        media_education_ids.append(education_media.id)
    education_dict["media_education_ids"] = media_education_ids

    return education_dict


def get_all_educations(user_id):
    educations = backend.get_all_educations(user_id)
    educations_list = []
    for education in educations:
        education_dict = education.to_dict()

        # medias
        media_education_ids = []
        for education_media in education.medias:
            media_education_ids.append(education_media.id)
        education_dict["media_education_ids"] = media_education_ids

        educations_list += [education_dict]

    return educations_list


def update_education(education_data, user_id, education_id):
    education = backend.update_education(education_data, user_id, education_id)
    education_dict = education.to_dict()

    return education_dict


def delete_education(user_id, education_id):
    backend.delete_education(user_id, education_id)
