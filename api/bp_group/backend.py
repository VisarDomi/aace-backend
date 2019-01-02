from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound, MissingArguments

from ..common.models import Group
from ..common.models import User


def create_group(group_data):

    if group_data['name'] is None: 
        msg = "Please provide an name."
        raise MissingArguments(message=msg)

    group = Group(**group_data)
    group.save()

    print("The group is: ", group)
    # try:
    #     print('group saved')
    # except IntegrityError:
    #     msg = 'Group `%s` has been already created.' % group_data['name']
    #     raise RecordAlreadyExists(message=msg)

    return group



def get_group_by_id(group_id):
    try:
        result = Group.query.filter(Group.id == group_id).one()
    except NoResultFound:
        msg = 'There is no Group with `id: %s`' % id
        raise RecordNotFound(message=msg)

    return result

def get_group(group_id):
    group = get_group_by_id(group_id)
    return group

def get_all_groups():
    return Group.query.all()


def update_group(group_data, group_id):
    group = get_group_by_id(group_id)
    group.update(**group_data)
    return group


def delete_group(group_id):
    group = get_group_by_id(group_id)
    group.delete()

def remove_user_from_group(group_data, group_id):
    group = get_group_by_id(group_id)
    user = User.query.filter(User.id == group_data['user_id']).one()
    group.users.remove(user)
    group.save()
    return group


def add_user_to_group(group_data, group_id):
    group = get_group_by_id(group_id)
    user = User.query.filter(User.id == group_data['user_id']).one()
    group.users.append(user)
    group.save()
    return group


