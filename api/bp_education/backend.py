from flask import g
from ..models.items import Education
from ..common.exceptions import (
    CannotChangeOthersProfile,
    CannotDeleteOthersEducation,
)
from ..bp_media_education.backend import delete_media, get_medias
from ..helper_functions.get_by_id import get_education_by_id


def create_education(education_data, user_id):
    if int(user_id) == g.current_user.id:
        education = Education(**education_data)
        education.user = g.current_user
        education.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return education


def get_educations(user_id):
    educations = Education.query.filter(Education.user_id == user_id).all()

    return educations


def update_education(education_data, user_id, education_id):
    if int(user_id) == g.current_user.id:
        education = get_education_by_id(education_id)
        education.update(**education_data)
        education.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return education


def delete_education(user_id, education_id):

    if int(user_id) == g.current_user.id:

        medias = get_medias(user_id, education_id)
        for media in medias:
            delete_media(user_id, media.id)
        education = get_education_by_id(education_id)
        education.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersEducation(message=msg)
