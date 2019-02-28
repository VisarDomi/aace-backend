from flask import g
from ..common.models import Education
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotDeleteOthersEducation,
)
from ..bp_user.backend import get_user_by_id


def create_education(education_data, user_id):
    if int(user_id) == g.current_user.id:
        education = Education(**education_data)
        education.user = g.current_user
        education.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return education


def get_education_by_id(education_id):
    try:
        education = Education.query.filter(Education.id == education_id).one()
    except NoResultFound:
        msg = f"There is no education with id {education_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {education_id}`"
        raise InvalidURL(message=msg)
    return education


def get_all_educations(user_id):
    educations = Education.query.filter(Education.user_id == user_id).all()
    return educations


def update_education(education_data, user_id, education_id):
    if int(user_id) == g.current_user.id:
        education = get_education_by_id(education_id)
        education.update_from_dict(education_data)
        education.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return education


def delete_education(user_id, education_id):
    user = get_user_by_id(user_id)
    education = get_education_by_id(education_id)
    if user.email == g.current_user.email:
        education.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersEducation(message=msg)
