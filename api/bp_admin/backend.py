from flask import g, send_from_directory  # , send_file
from functools import wraps
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordNotFound
from ..common.exceptions import (
    YouAreNotAdmin,
    CannotChangeFirstAdminProperties,
    InvalidURL,
)

from ..common.models import User, MediaEducation
from config import Config


# create a custom decorator, so only admins can use the following functions
def are_you_admin(a_function):
    @wraps(a_function)
    def decorated_function(*args, **kwargs):
        if g.current_user.role == "admin":
            return a_function(*args, **kwargs)  # here goes the function
        else:
            msg = "You are not an admin."
            raise YouAreNotAdmin(message=msg)

    return decorated_function


@are_you_admin
def get_user_by_id(user_id):
    try:
        user = User.query.filter(User.id == int(user_id)).one()
    except NoResultFound:
        msg = f"There is no User with `id: {user_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {user_id}`"
        raise InvalidURL(message=msg)
    return user


@are_you_admin
def get_approved_users():
    users = User.query.filter(User.register_status == "approved").all()
    return users


@are_you_admin
def get_applying_users():
    users = User.query.filter(User.register_status == "applying").all()
    return users


@are_you_admin
def get_rejected_users():
    users = User.query.filter(User.register_status == "rejected").all()
    return users


@are_you_admin
def get_rebutted_users():
    users = User.query.filter(User.register_status == "rebutted").all()
    return users


@are_you_admin
def get_reapplying_users():
    users = User.query.filter(User.register_status == "reapplying").all()
    return users


@are_you_admin
def get_blank_users():
    users = User.query.filter(User.register_status == "blank").all()
    return users


@are_you_admin
def update_user(user_data, user_id):

    secure = True
    if secure:
        if int(user_id) != 1:
            user = get_user_by_id(user_id)
            user.update(**user_data)
            user.save()
            return user
        else:
            msg = "Cannot change admin with `id: %s`" % user_id
            raise CannotChangeFirstAdminProperties(message=msg)
    else:
        user = get_user_by_id(user_id)
        user.update(**user_data)
        user.save()
        return user


# download section


def get_media_by_id(media_education_id):
    try:
        media = MediaEducation.query.filter(
            MediaEducation.id == media_education_id
        ).one()
    except NoResultFound:
        msg = f"There is no media with id {media_education_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_education_id}`"
        raise InvalidURL(message=msg)

    return media


@are_you_admin
def download_education(media_education_id):
    media = get_media_by_id(media_education_id)
    directory = Config.UPLOADED_EDUCATIONFILES_DEST
    filename = media.media_filename
    download_file = send_from_directory(directory, filename, as_attachment=True)
    return download_file
