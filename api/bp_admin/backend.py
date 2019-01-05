from flask import g
from functools import wraps
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound
from ..common.exceptions import YouAreNotAdmin

from ..common.models import User


#create a custom decorator, so only admins can use the following functions
def are_you_admin(a_function):
    @wraps(a_function)
    def decorated_function(*args, **kwargs):
        if g.current_user.role == 'admin':
            return a_function(*args, **kwargs)  #here goes the function
        else:
            msg = 'You are not an admin.'
            raise YouAreNotAdmin(message=msg)
    return decorated_function


@are_you_admin
def create_user(user_data):
    user = User(**user_data)
    try:
        user.save()
    except IntegrityError:
        msg = 'Email `%s` already has been taken' % user_data['email']
        raise RecordAlreadyExists(message=msg)
    return user


@are_you_admin
def get_user_by_id(user_id):
    try:
        result = User.query.filter(User.id == user_id).one()
    except NoResultFound:
        msg = 'There is no User with `id: %s`' % id
        raise RecordNotFound(message=msg)
    return result


@are_you_admin
def get_all_users():
    return User.query.all()


@are_you_admin
def update_user(user_data, user_id):
    user = get_user_by_id(user_id)
    user.update(**user_data)
    return user


@are_you_admin
def delete_user(user_id):
    user = get_user_by_id(user_id)
    user.delete()
