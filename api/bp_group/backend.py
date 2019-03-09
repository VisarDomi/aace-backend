from ..common.models import Group, User
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    UserIsAlreadyPartOfGroup,
    ThereIsAlreadyAGroupByThatName,
    NoUserByThatID,
    InvalidURL,
)
from ..bp_admin.backend import admin_required
from ..bp_user.backend import get_user_by_id


@admin_required
def create_group(group_data):
    is_group = Group.query.filter(Group.name == group_data["name"]).one_or_none()
    if is_group:
        msg = "There is already a group with the name '% s'" % is_group.name
        raise ThereIsAlreadyAGroupByThatName(message=msg)
    else:
        group = Group(**group_data)
        group.save()

    return group


def get_group_by_id(group_id):
    try:
        group = Group.query.filter(Group.id == group_id).one()
    except NoResultFound:
        msg = f"There is no group with id {group_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {group_id}`"
        raise InvalidURL(message=msg)
    return group


def get_all_groups():
    groups = Group.query.all()

    return groups


@admin_required
def update_group(group_data, group_id):
    is_group = Group.query.filter(Group.name == group_data["name"]).one_or_none()
    group = get_group_by_id(group_id)
    if is_group and is_group != group:
        msg = "There is already a group with the name '% s'" % is_group.name
        raise ThereIsAlreadyAGroupByThatName(message=msg)
    else:
        group.update(**group_data)
        group.save()

    return group


@admin_required
def delete_group(group_id):
    group = get_group_by_id(group_id)
    group.delete()


def get_users_from_group(group_id):
    group = get_group_by_id(group_id)
    users = group.users.all()

    return users


@admin_required
def add_user_to_group(group_id, user_id):
    group = get_group_by_id(group_id)
    user = get_user_by_id(user_id)
    if user != group.users.filter(User.id == user_id).one_or_none():
        group.users.append(user)
        group.save()
    else:
        msg = "User % s is already part of the group % s." % (user_id, group_id)
        raise UserIsAlreadyPartOfGroup(message=msg)
    return group


@admin_required
def remove_user_from_group(group_id, user_id):
    group = get_group_by_id(group_id)
    user = group.users.filter(User.id == user_id).one_or_none()
    if user is not None:
        user = get_user_by_id(user_id)
        group.users.remove(user)
        group.save()
    else:
        msg = "User with `id: %s` is not part of the group with `id %s`." % (
            user_id,
            group_id,
        )
        raise NoUserByThatID(message=msg)
