from flask import g
from ..common.exceptions import (
    OrganizationGroupIsAlreadyPartOfGroup,
    NoOrganizationGroupByThatID,
)
from ..models.items import Event, OrganizationGroup
from ..bp_media_event.backend import get_medias, delete_media
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_event_by_id, get_organizationgroup_by_id
# from ..helper_functions.email import send_email_to_users


@admin_required
def create_event(event_data):
    event = Event(**event_data)
    event.author = g.current_user
    event.save()

    return event


def get_events():
    events = Event.query.all()
    allowed_events = []
    if g.current_user.role == "admin":
        allowed_events = events
    else:
        for event in events:
            for group in event.organizationgroups.all():
                if g.current_user in group.users.all():
                    allowed_events.append(event)

    return allowed_events


@admin_required
def update_event(event_data, event_id):
    event = get_event_by_id(event_id)
    event.update(**event_data)
    event.save()

    return event


@admin_required
def delete_event(event_id):
    for media in get_medias(event_id):
        delete_media(media.id)
    event = get_event_by_id(event_id)
    event.delete()


# Getting, adding, removing group from event


def get_organizationgroups_from_event(event_id):
    event = get_event_by_id(event_id)
    organizationgroups = event.organizationgroups.all()

    return organizationgroups


def filter_og_of_oc(event, organizationgroup_id, OrganizationGroup):
    """Filter organizationgroups of event"""
    is_og_in_oc = event.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()

    return is_og_in_oc


def group_in_event_or_none(
    organizationgroup, event, organizationgroup_id, OrganizationGroup
):
    group_or_none = organizationgroup == filter_og_of_oc(
        event, organizationgroup_id, OrganizationGroup
    )

    return group_or_none


def is_group_in_event(
    organizationgroup, event, organizationgroup_id, OrganizationGroup
):
    organizationgroup_in_a_event = None
    if group_in_event_or_none(
        organizationgroup, event, organizationgroup_id, OrganizationGroup
    ):
        organizationgroup_in_a_event = organizationgroup

    return organizationgroup_in_a_event


@admin_required
def add_organizationgroup_to_event(event_id, organizationgroup_id):
    organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
    event = get_event_by_id(event_id)
    organizationgroup_in_a_event_or_none = is_group_in_event(
        organizationgroup, event, organizationgroup_id, OrganizationGroup
    )
    if organizationgroup is not organizationgroup_in_a_event_or_none:
        event = get_event_by_id(event_id)
        event.organizationgroups.append(organizationgroup)
        event.save()
    else:
        msg = "OrganizationGroup % s is already part of the event % s." % (
            organizationgroup_id,
            event_id,
        )
        raise OrganizationGroupIsAlreadyPartOfGroup(message=msg)

    return event


@admin_required
def remove_organizationgroup_from_event(event_id, organizationgroup_id):
    event = get_event_by_id(event_id)
    organizationgroup = event.organizationgroups.filter(
        OrganizationGroup.id == organizationgroup_id
    ).one_or_none()
    if organizationgroup is not None:
        organizationgroup = get_organizationgroup_by_id(organizationgroup_id)
        event.organizationgroups.remove(organizationgroup)
        event.save()
    else:
        msg = (
            f"OrganizationGroup with `id: {organizationgroup_id}` is not part "
            f"of the event with `id {event_id}`."
        )
        raise NoOrganizationGroupByThatID(message=msg)


@admin_required
def send_email(event_id):
    # send_email_to_users(event_id) doesn't work, needs copy paste
    print("event_id", event_id)
