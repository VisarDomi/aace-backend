from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    UserIsAlreadyPartOfGroup,
    ThereIsAlreadyAGroupByThatName,
    NoUserByThatID,
)


from ..common.models import OrganizationGroup, User

from ..bp_media_organizationgroup.backend import get_all_medias, delete_media
from ..bp_admin.backend import are_you_admin
from ..bp_user.backend import get_user_by_id


@are_you_admin
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


def get_organizationgroup_by_id(organizationgroup_id):
    try:
        organizationgroup = OrganizationGroup.query.filter(
            OrganizationGroup.id == organizationgroup_id
        ).one()
    except NoResultFound:
        msg = f"There is no OrganizationGroup with `id: {organizationgroup_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {organizationgroup_id}`"
        raise InvalidURL(message=msg)

    return organizationgroup


def get_all_organizationgroups():
    organizationgroups = OrganizationGroup.query.all()

    return organizationgroups


@are_you_admin
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


@are_you_admin
def delete_organizationgroup(organizationgroup_id):
    for media in get_all_medias(organizationgroup_id):
        delete_media(organizationgroup_id, media.id)
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    organizationgroup.delete()


def get_users_from_organizationgroup(organizationgroup_id):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    users = organizationgroup.users.all()

    return users


@are_you_admin
def add_user_to_organizationgroup(organizationgroup_id, user_id):
    user = get_user_by_id(user_id)
    organizationgroups = get_all_organizationgroups()
    user_in_a_group = None
    for group in organizationgroups:
        if user == group.users.filter(User.id == user_id).one_or_none():
            user_in_a_group = user
            that_group_id = group.id
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


@are_you_admin
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
