from flask import g
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import (
    RecordAlreadyExists,
    RecordNotFound,
    MissingArguments,
    CannotChangeOthersProfile,
    CannotDeleteOthersProfile,
    CannotDeleteFirstAdmin,
    InvalidURL,
)

from ..common.models import User
from ..bp_skill.backend import get_all_skills, delete_skill
from ..bp_experience.backend import get_all_experiences, delete_experience
from ..bp_education.backend import get_all_educations, delete_education
from ..bp_media_user.backend import get_all_medias, delete_media


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
        user.save()

    else:
        msg = "You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return user


def delete_user(user_id):
    if int(user_id) != 1:
        if int(user_id) == g.current_user.id:
            for media in get_all_medias(user_id):
                delete_media(user_id, media.id)
            for education in get_all_educations(user_id):
                delete_education(user_id, education.id)
            for experience in get_all_experiences(user_id):
                delete_experience(user_id, experience.id)
            for skill in get_all_skills(user_id):
                delete_skill(user_id, skill.id)
            user = get_user_by_id(user_id)
            user.delete()
        else:
            msg = "You can't delete other people's profile."
            raise CannotDeleteOthersProfile(message=msg)
    else:
        msg = "Cannot delete admin with `id: %s`" % user_id
        raise CannotDeleteFirstAdmin(message=msg)
