from flask import g
from ..common.exceptions import (
    OrganizationGroupIsAlreadyPartOfGroup,
    NoOrganizationGroupByThatID,
)
from ..common.models.items import Communication, OrganizationGroup
from ..bp_media_communication.backend import get_all_medias, delete_media
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import (
    get_communication_by_id,
    get_organizationgroup_by_id,
)
from ..helper_functions.email import send_email_to_users


@admin_required
def create_communication(communication_data):
    communication = Communication(**communication_data)
    communication.author = g.current_user
    communication.save()

    return communication


def get_all_communications():
    communications = Communication.query.all()
    allowed_communications = []
    if g.current_user.role == "admin":
        allowed_communications = communications
    else:
        for communication in communications:
            for group in communication.organizationgroups.all():
                if g.current_user in group.users.all():
                    allowed_communications.append(communication)

    return allowed_communications


@admin_required
def update_communication(communication_data, communication_id):
    communication = get_communication_by_id(communication_id)
    communication.update(**communication_data)
    communication.save()

    return communication


@admin_required
def delete_communication(communication_id):
    for media in get_all_medias(communication_id):
        delete_media(communication_id, media.id)
    communication = get_communication_by_id(communication_id)
    communication.delete()


# Getting, adding, removing group from communication


def get_organizationgroups_from_communication(communication_id):
    communication = get_communication_by_id(communication_id)
    organizationgroups = communication.organizationgroups.all()

    return organizationgroups


def filter_og_of_oc(
    communication, organizationgroup_id, OrganizationGroup
):
    """Filter organizationgroups of communication"""
    is_og_in_oc = communication.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()

    return is_og_in_oc


def group_in_communication_or_none(
    organizationgroup, communication, organizationgroup_id, OrganizationGroup
):
    group_or_none = (
        organizationgroup
        == filter_og_of_oc(
            communication, organizationgroup_id, OrganizationGroup
        )
    )

    return group_or_none


def is_group_in_communication(
    organizationgroup, communication, organizationgroup_id, OrganizationGroup
):
    organizationgroup_in_a_communication = None
    if group_in_communication_or_none(
        organizationgroup,
        communication,
        organizationgroup_id,
        OrganizationGroup,
    ):
        organizationgroup_in_a_communication = organizationgroup

    return organizationgroup_in_a_communication


@admin_required
def add_organizationgroup_to_communication(
    communication_id, organizationgroup_id
):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    communication = get_communication_by_id(communication_id)
    organizationgroup_in_a_communication_or_none = is_group_in_communication(
        organizationgroup,
        communication,
        organizationgroup_id,
        OrganizationGroup,
    )
    if organizationgroup is not organizationgroup_in_a_communication_or_none:
        communication = get_communication_by_id(
            communication_id
        )
        communication.organizationgroups.append(organizationgroup)
        communication.save()
    else:
        msg = (
            "OrganizationGroup % s is already part of the communication % s."
            % (organizationgroup_id, communication_id)
        )
        raise OrganizationGroupIsAlreadyPartOfGroup(message=msg)

    return communication


@admin_required
def remove_organizationgroup_from_communication(
    communication_id, organizationgroup_id
):
    communication = get_communication_by_id(communication_id)
    organizationgroup = communication.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()
    if organizationgroup is not None:
        organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
        communication.organizationgroups.remove(organizationgroup)
        communication.save()
    else:
        msg = (
            f"OrganizationGroup with `id: {organizationgroup_id}` is not part "
            f"of the communication with `id {communication_id}`."
        )
        raise NoOrganizationGroupByThatID(message=msg)


@admin_required
def send_email(communication_id):
    send_email_to_users(communication_id)
