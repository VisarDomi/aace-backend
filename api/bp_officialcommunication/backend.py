from flask import g
from ..common.exceptions import (
    OrganizationGroupIsAlreadyPartOfGroup,
    NoOrganizationGroupByThatID,
)
from ..common.models import OfficialCommunication, OrganizationGroup
from ..bp_media_officialcommunication.backend import get_all_medias, delete_media
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import (
    get_officialcommunication_by_id,
    get_organizationgroup_by_id,
)
from ..helper_functions.email import send_email_to_users


@admin_required
def create_officialcommunication(officialcommunication_data):
    officialcommunication = OfficialCommunication(**officialcommunication_data)
    officialcommunication.author = g.current_user
    officialcommunication.save()

    return officialcommunication


def get_all_officialcommunications():
    officialcommunications = OfficialCommunication.query.all()
    allowed_officialcommunications = []
    if g.current_user.role == "admin":
        allowed_officialcommunications = officialcommunications
    else:
        for communication in officialcommunications:
            for group in communication.organizationgroups.all():
                if g.current_user in group.users.all():
                    allowed_officialcommunications.append(communication)

    return allowed_officialcommunications


@admin_required
def update_officialcommunication(officialcommunication_data, officialcommunication_id):
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    officialcommunication.update(**officialcommunication_data)
    officialcommunication.save()

    return officialcommunication


@admin_required
def delete_officialcommunication(officialcommunication_id):
    for media in get_all_medias(officialcommunication_id):
        delete_media(officialcommunication_id, media.id)
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    officialcommunication.delete()


# Getting, adding, removing group from communication


def get_organizationgroups_from_officialcommunication(officialcommunication_id):
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    organizationgroups = officialcommunication.organizationgroups.all()

    return organizationgroups


def filter_organizationgroups_of_officialcommunication(
    officialcommunication, organizationgroup_id, OrganizationGroup
):
    is_gr_in_co = officialcommunication.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()

    return is_gr_in_co


def group_in_communication_or_none(
    organizationgroup, officialcommunication, organizationgroup_id, OrganizationGroup
):
    group_or_none = (
        organizationgroup
        == filter_organizationgroups_of_officialcommunication(
            officialcommunication, organizationgroup_id, OrganizationGroup
        )
    )

    return group_or_none


def is_group_in_communication(
    organizationgroup, officialcommunication, organizationgroup_id, OrganizationGroup
):
    organizationgroup_in_a_officialcommunication = None
    if group_in_communication_or_none(
        organizationgroup,
        officialcommunication,
        organizationgroup_id,
        OrganizationGroup,
    ):
        organizationgroup_in_a_officialcommunication = organizationgroup

    return organizationgroup_in_a_officialcommunication


@admin_required
def add_organizationgroup_to_officialcommunication(
    officialcommunication_id, organizationgroup_id
):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    organizationgroup_in_a_officialcommunication_or_none = is_group_in_communication(
        organizationgroup,
        officialcommunication,
        organizationgroup_id,
        OrganizationGroup,
    )
    if organizationgroup is not organizationgroup_in_a_officialcommunication_or_none:
        officialcommunication = get_officialcommunication_by_id(
            officialcommunication_id
        )
        officialcommunication.organizationgroups.append(organizationgroup)
        officialcommunication.save()
    else:
        msg = (
            "OrganizationGroup % s is already part of the officialcommunication % s."
            % (organizationgroup_id, officialcommunication_id)
        )
        raise OrganizationGroupIsAlreadyPartOfGroup(message=msg)

    return officialcommunication


@admin_required
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


@admin_required
def send_email(officialcommunication_id):
    send_email_to_users(officialcommunication_id)
