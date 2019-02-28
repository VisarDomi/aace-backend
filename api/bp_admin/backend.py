from flask import g, send_from_directory, send_file
from functools import wraps
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordNotFound
from ..common.exceptions import (
    YouAreNotAdmin,
    CannotChangeFirstAdminProperties,
    CannotDeleteFirstAdmin,
    InvalidURL,
)

from ..common.models import User
from ..bp_media.backend import get_media_by_id
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
def get_applying_users():
    users = User.query.filter(User.register_status == "approved").all()
    return users


@are_you_admin
def get_applying_users():
    users = (
        User.query.filter(User.register_status != "blank")
        .filter(User.register_status != "approved")
        .all()
    )
    return users


@are_you_admin
def update_user(user_data, user_id):
    # user = get_user_by_id(user_id)
    # user.update_flusk(**user_data)
    # user.save()
    # return user

    secure = False
    if secure:
        if int(user_id) != 1:
            user = get_user_by_id(user_id)
            user.update_from_dict(user_data)
            user.save()
            return user
        else:
            msg = "Cannot change admin with `id: %s`" % user_id
            raise CannotChangeFirstAdminProperties(message=msg)
    else:
        user = get_user_by_id(user_id)
        user.update_from_dict(user_data)
        user.save()
        return user


@are_you_admin
def delete_user(user_id):
    if int(user_id) != 1:
        user = get_user_by_id(user_id)
        user.delete()
    else:
        msg = "Cannot delete admin with `id: %s`" % user_id
        raise CannotDeleteFirstAdmin(message=msg)


def download(media_id):
    media = get_media_by_id(media_id)
    directory = Config.UPLOADED_FILES_DEST
    filename = media.media_filename
    download_file = send_from_directory(directory, filename, as_attachment=True)
    return download_file
