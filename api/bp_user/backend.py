from flask import g
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound, MissingArguments
from ..common.exceptions import CannotChangeOthersProfile, CannotDeleteOthersProfile

from ..common.models import User



def create_user(user_data):
    if user_data['email'] is None or user_data['password'] is None: 
        msg = "Please provide an email and a password."
        raise MissingArguments(message=msg)
    user = User(**user_data)
    user.set_password(user_data['password'])
    try:
        user.save()
    except IntegrityError:
        msg = 'Email `%s` is already in use for another account.' % user_data['email']
        raise RecordAlreadyExists(message=msg)
    if user.id == 1:
        user.role = 'admin'
        user.save()
    return user


def get_user_by_id(user_id):
    try:
        result = User.query.filter(User.id == user_id).one()
    except NoResultFound:
        msg = 'There is no User with `id: %s`' % user_id
        raise RecordNotFound(message=msg)
    return result


def get_all_users():
    return User.query.all()


def update_user(user_data, user_id):
    user = get_user_by_id(user_id)
    if user.email == g.current_user.email:
        user.update(**user_data)
        return user
    else:
        msg = "You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)


def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user.email == g.current_user.email:
        user.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersProfile(message=msg)
