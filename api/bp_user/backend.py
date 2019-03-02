from flask import g
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound, MissingArguments
from ..common.exceptions import CannotChangeOthersProfile, CannotDeleteOthersProfile
from ..common.exceptions import CannotDeleteFirstAdmin, InvalidURL

from ..common.models import User
from ..bp_education.backend import get_all_educations, delete_education


def create_user(user_data):
    if user_data["email"] is None or user_data["password"] is None:
        msg = "Please provide an email and a password."
        raise MissingArguments(message=msg)
    if not User.query.filter(User.email == user_data["email"]).one_or_none():
        user = User(**user_data)
        user.set_password(user_data["password"])
        user.save()
    else:
        msg = "Email `%s` is already in use for another account." % user_data["email"]
        raise RecordAlreadyExists(message=msg)
    if user.id == 1:
        user.role = "admin"
        user.save()
    user.get_token(expires_in=36_000_000)
    return user


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


def get_all_users():
    users = User.query.all()
    return users


def update_user(user_data, user_id):
    if int(user_id) == g.current_user.id:
        user = get_user_by_id(user_id)
        user.update(**user_data)
        user.register_status = "reapplying"
        user.save()
        return user
    else:
        msg = "You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)


def delete_user(user_id):
    if int(user_id) != 1:
        if int(user_id) == g.current_user.id:
            for education in get_all_educations(user_id):
                delete_education(user_id, education.id)
            user = get_user_by_id(user_id)
            print("user.delete() :", user)
            user.delete()
        else:
            msg = "You can't delete other people's profile."
            raise CannotDeleteOthersProfile(message=msg)
    else:
        msg = "Cannot delete admin with `id: %s`" % user_id
        raise CannotDeleteFirstAdmin(message=msg)
