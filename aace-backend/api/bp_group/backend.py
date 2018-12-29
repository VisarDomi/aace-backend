from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound, MissingArguments

from ..common.models import Group
from ..common.models import User


def create_group(group_data):

    if group_data['name'] is None: 
        msg = "Please provide an name."
        raise MissingArguments(message=msg)
    # if Group.query.filter_by(email = group_data['email']).first() is not None: 
    #     print("existing group")
    #     # abort(400) #existing group
    
    group = Group(**group_data)
    print("The group is: ", group)
    try:
        group.save()
    except IntegrityError:
        msg = 'Group `%s` has been already created.' % group_data['name']
        raise RecordAlreadyExists(message=msg)

    return group

def return_group(group):
    users = group.users.all()
    group = group.to_dict()
    users = {x.id: x.to_dict() for x in users}
    return_object = {
                        "group_data" : {**group},
                        "users" : {**users}
                    }
    return return_object

def get_group_by_id(group_id):
    try:
        result = Group.query.filter(Group.id == group_id).one()
    except NoResultFound:
        msg = 'There is no Group with `id: %s`' % id
        raise RecordNotFound(message=msg)

    return result

def get_group(group_id):
    group = get_group_by_id(group_id)
    group = return_group(group)
    return group

def get_all_groups():
    return Group.query.all()


def update_group(group_data, group_id):
    group = get_group_by_id(group_id)
    group.update(**group_data)
    group = return_group(group)
    return group


def delete_group(group_id):
    group = get_group_by_id(group_id)
    group.delete()

def add_user_to_group(group_data, group_id):
    group = get_group_by_id(group_id)
    user = User.query.filter(User.id == group_data['user_id']).one()
    group.users.append(user)
    group.save()
    group = return_group(group)
    return group

def remove_user_to_group(group_data, group_id):
    group = get_group_by_id(group_id)
    user = User.query.filter(User.id == group_data['user_id']).one()
    group.users.remove(user)
    group.save()
    group = return_group(group)
    return group

