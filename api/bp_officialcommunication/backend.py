from flask import g
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    OrganizationGroupIsAlreadyPartOfGroup,
    ThereIsAlreadyAGroupByThatName,
    NoOrganizationGroupByThatID,
)


from ..common.models import OfficialCommunication, OrganizationGroup

from ..bp_media_officialcommunication.backend import get_all_medias, delete_media
from ..bp_admin.backend import are_you_admin
from ..bp_organizationgroup.backend import get_organizationgroup_by_id


@are_you_admin
def create_officialcommunication(officialcommunication_data):
    is_communication = OfficialCommunication.query.filter(
        OfficialCommunication.name == officialcommunication_data["name"]
    ).one_or_none()
    if is_communication:
        msg = "There is already a group with the name '% s'" % is_communication.name
        raise ThereIsAlreadyAGroupByThatName(message=msg)
    else:
        officialcommunication = OfficialCommunication(**officialcommunication_data)
        officialcommunication.author = g.current_user
        officialcommunication.save()

    return officialcommunication


def get_officialcommunication_by_id(officialcommunication_id):
    try:
        officialcommunication = OfficialCommunication.query.filter(
            OfficialCommunication.id == officialcommunication_id
        ).one()
    except NoResultFound:
        msg = f"There is no OfficialCommunication with `id: {officialcommunication_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {officialcommunication_id}`"
        raise InvalidURL(message=msg)

    return officialcommunication


def get_all_officialcommunications():
    officialcommunications = OfficialCommunication.query.all()

    return officialcommunications


@are_you_admin
def update_officialcommunication(officialcommunication_data, officialcommunication_id):
    is_communication = OfficialCommunication.query.filter(
        OfficialCommunication.name == officialcommunication_data["name"]
    ).one_or_none()
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    if is_communication and is_communication != officialcommunication:
        msg = "There is already a group with the name '% s'" % is_communication.name
        raise ThereIsAlreadyAGroupByThatName(message=msg)
    else:
        officialcommunication.update(**officialcommunication_data)
        officialcommunication.save()

    return officialcommunication


@are_you_admin
def delete_officialcommunication(officialcommunication_id):
    for media in get_all_medias(officialcommunication_id):
        delete_media(officialcommunication_id, media.id)
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    officialcommunication.delete()


def get_organizationgroups_from_officialcommunication(officialcommunication_id):
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    organizationgroups = officialcommunication.organizationgroups.all()

    return organizationgroups


@are_you_admin
def add_organizationgroup_to_officialcommunication(
    officialcommunication_id, organizationgroup_id
):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    officialcommunications = get_all_officialcommunications()
    organizationgroup_in_a_group = None
    for group in officialcommunications:
        if (
            organizationgroup
            == group.organizationgroups.filter(
                OrganizationGroup.id == organizationgroup_id
            ).one_or_none()
        ):
            organizationgroup_in_a_group = organizationgroup
            that_group_id = group.id
    if organizationgroup is not organizationgroup_in_a_group:
        officialcommunication = get_officialcommunication_by_id(
            officialcommunication_id
        )
        officialcommunication.organizationgroups.append(organizationgroup)
        officialcommunication.save()
    else:
        msg = (
            "OrganizationGroup % s is already part of the officialcommunication % s."
            % (organizationgroup_id, that_group_id)
        )
        raise OrganizationGroupIsAlreadyPartOfGroup(message=msg)

    return officialcommunication


@are_you_admin
def remove_organizationgroup_from_officialcommunication(
    officialcommunication_id, organizationgroup_id
):
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    organizationgroup = officialcommunication.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()
    if organizationgroup is not None:
        organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
        officialcommunication.organizationgroups.remove(organizationgroup)
        officialcommunication.save()
    else:
        msg = (
            f"OrganizationGroup with `id: {organizationgroup_id}` is not part "
            f"of the officialcommunication with `id {officialcommunication_id}`."
        )
        raise NoOrganizationGroupByThatID(message=msg)
