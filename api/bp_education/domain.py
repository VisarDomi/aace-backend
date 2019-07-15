from . import backend
from ..helper_functions.get_by_id import get_education_by_id


def create_education(education_data, user_id):
    education = backend.create_education(education_data, user_id)
    education_dict = education.to_dict()

    return education_dict


def get_educations(user_id):
    educations = backend.get_educations(user_id)
    educations_list = []
    for education in educations:
        education_dict = education.to_dict()

        education_medias = []
        for education_media in education.medias:
            education_medias.append(education_media.to_dict())
        education_dict["education_medias"] = education_medias

        educations_list += [education_dict]

    return educations_list


def get_education(education_id):
    education = get_education_by_id(education_id)
    education_dict = education.to_dict()

    education_medias = []
    for education_media in education.medias:
        education_medias.append(education_media.to_dict())
    education_dict["education_medias"] = education_medias

    return education_dict


def update_education(education_data, user_id, education_id):
    education = backend.update_education(education_data, user_id, education_id)
    education_dict = education.to_dict()

    return education_dict


def delete_education(user_id, education_id):
    backend.delete_education(user_id, education_id)
