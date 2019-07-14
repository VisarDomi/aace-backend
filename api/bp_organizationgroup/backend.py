from ..common.exceptions import (
    UserIsAlreadyPartOfGroup,
    ThereIsAlreadyAGroupByThatName,
    NoUserByThatID,
)
from ..common.models.items import OrganizationGroup
from ..common.models.users import User
from ..bp_media_organizationgroup.backend import get_all_medias, delete_media
from ..bp_user.backend import get_user_by_id
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_organizationgroup_by_id


@admin_required
def create_organizationgroup(organizationgroup_data):
    is_group = OrganizationGroup.query.filter(
        OrganizationGroup.name == organizationgroup_data["name"]
    ).one_or_none()
    if is_group:
        msg = "There is already a group with the name '% s'" % is_group.name
        raise ThereIsAlreadyAGroupByThatName(message=msg)
    else:
        organizationgroup = OrganizationGroup(**organizationgroup_data)
        organizationgroup.save()

    return organizationgroup


def get_all_organizationgroups():
    organizationgroups = OrganizationGroup.query.all()

    return organizationgroups


@admin_required
def update_organizationgroup(organizationgroup_data, organizationgroup_id):
    is_group = OrganizationGroup.query.filter(
        OrganizationGroup.name == organizationgroup_data["name"]
    ).one_or_none()
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    if is_group and is_group != organizationgroup:
        msg = "There is already a group with the name '% s'" % is_group.name
        raise ThereIsAlreadyAGroupByThatName(message=msg)
    else:
        organizationgroup.update(**organizationgroup_data)
        organizationgroup.save()

    return organizationgroup


@admin_required
def delete_organizationgroup(organizationgroup_id):
    for media in get_all_medias(organizationgroup_id):
        delete_media(organizationgroup_id, media.id)
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    organizationgroup.delete()


def get_users_from_organizationgroup(organizationgroup_id):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    users = organizationgroup.users.all()

    return users


@admin_required
def unassigned_users():
    organizationgroups = OrganizationGroup.query.all()
    users = User.query.all()
    unassigned_users = []
    users_in_a_group = []
    for organizationgroup in organizationgroups:
        for user in users:
            user_in_organizationgroup = organizationgroup.users.filter(
                User.id == user.id
            ).one_or_none()
            if user_in_organizationgroup:
                users_in_a_group += [user_in_organizationgroup]
    for user in users:
        if user not in users_in_a_group and user.application_status == 'accepted':
            unassigned_users += [user]

    return unassigned_users


def add_one_user_to_an_organizationgroup(organizationgroup_id, user_id):
    user = get_user_by_id(user_id)
    organizationgroups = get_all_organizationgroups()
    user_in_a_group = None
    for organizationgroup in organizationgroups:
        if user == organizationgroup.users.filter(User.id == user_id).one_or_none():
            user_in_a_group = user
            that_group_id = organizationgroup.id
    if user is not user_in_a_group:
        organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
        organizationgroup.users.append(user)
        organizationgroup.save()
    else:
        msg = "User % s is already part of the organizationgroup % s." % (
            user_id,
            that_group_id,
        )
        raise UserIsAlreadyPartOfGroup(message=msg)

    return organizationgroup


@admin_required
def add_user_to_organizationgroup(organizationgroup_id, user_id):
    organizationgroup = add_one_user_to_an_organizationgroup(
        organizationgroup_id, user_id
    )

    return organizationgroup


@admin_required
def remove_user_from_organizationgroup(organizationgroup_id, user_id):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    user = organizationgroup.users.filter(User.id == user_id).one_or_none()
    if user is not None:
        user = get_user_by_id(user_id)
        organizationgroup.users.remove(user)
        organizationgroup.save()
    else:
        msg = (
            "User with `id: %s` is not part of the organizationgroup with `id %s`."
            % (user_id, organizationgroup_id)
        )
        raise NoUserByThatID(message=msg)


@admin_required
def add_users_to_organizationgroup(user_data_ids, organizationgroup_id):
    for user_id in user_data_ids["ids"]:
        organizationgroup = add_one_user_to_an_organizationgroup(
            organizationgroup_id, user_id
        )

    return organizationgroup


@admin_required
def remove_users_from_organizationgroup(user_data_ids, organizationgroup_id):
    for user_id in user_data_ids["ids"]:
        remove_user_from_organizationgroup(organizationgroup_id, user_id)
