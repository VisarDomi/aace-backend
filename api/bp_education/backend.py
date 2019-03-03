from flask import g
from ..common.models import Education, User
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotDeleteOthersEducation,
)
from ..bp_media_education.backend import delete_media, get_all_medias


def get_user_by_id(user_id):
    try:
        user = User.query.filter(User.id == user_id).one()
    except NoResultFound:
        msg = f"There is no User with `id: {user_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {user_id}`"
        raise InvalidURL(message=msg)

    return user


def user_edited(user_id):
    user = get_user_by_id(user_id)
    if user.register_status not in ["applying", "reapplying"]:
        user.register_status = "reapplying"
    user.save()


def create_education(education_data, user_id):
    if int(user_id) == g.current_user.id:
        education = Education(**education_data)
        education.user = g.current_user
        education.save()
        user_edited(user_id)
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
        education.update(**education_data)
        education.save()
        user_edited(user_id)
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return education


def delete_education(user_id, education_id):

    if int(user_id) == g.current_user.id:

        medias = get_all_medias(user_id, education_id)
        for media in medias:
            delete_media(user_id, media.id)
        education = get_education_by_id(education_id)
        education.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersEducation(message=msg)
