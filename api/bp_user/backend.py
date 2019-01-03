from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound, MissingArguments

from ..common.models import User
from ..common.database import db_session

def create_user(user_data):

    if user_data['email'] is None or user_data['password'] is None: 
        msg = "Please provide an email and a password."
        raise MissingArguments(message=msg)

    
    user = User(**user_data)
    print("backend.the user data is: ", user_data)
    print("backend.The created user is: ", user)
    user.set_password(user_data['password'])
    print("backend.The user is: ", user)
    try:
        user.save()
        print('backend.user saved')
        # db_session.commit()
    except IntegrityError:
        msg = 'Email `%s` is already in use for another account.' % user_data['email']
        raise RecordAlreadyExists(message=msg)

    return user


def get_user_by_id(user_id):
    try:
        result = User.query.filter(User.id == user_id).one()
    except NoResultFound:
        msg = 'There is no User with `id: %s`' % id
        raise RecordNotFound(message=msg)

    return result


def get_all_users():
    return User.query.all()


def update_user(user_data, user_id):
    user = get_user_by_id(user_id)
    user.update(**user_data)

    return user


def delete_user(user_id):
    user = get_user_by_id(user_id)
    user.delete()
