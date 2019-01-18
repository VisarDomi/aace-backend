from flask import g
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
        result = User.query.filter(User.id == user_id).one()
    except NoResultFound:
        msg = f"There is no User with `id: {user_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {user_id}`"
        raise InvalidURL(message=msg)
    return result


@are_you_admin
def get_all_users():
    return User.query.all()


@are_you_admin
def get_applying_users():
    users = (
        User.query.filter(User.register_status != "blank")
        .filter(User.register_status != "accepted")
        .all()
    )
    return users


@are_you_admin
def update_user(user_data, user_id):
    if int(user_id) != 1:
        user = get_user_by_id(user_id)
        user.update_from_dict(user_data)
        user.save()
        return user
    else:
        msg = "Cannot change admin with `id: %s`" % user_id
        raise CannotChangeFirstAdminProperties(message=msg)


@are_you_admin
def delete_user(user_id):
    if int(user_id) != 1:
        user = get_user_by_id(user_id)
        user.delete()
    else:
        msg = "Cannot delete admin with `id: %s`" % user_id
        raise CannotDeleteFirstAdmin(message=msg)
