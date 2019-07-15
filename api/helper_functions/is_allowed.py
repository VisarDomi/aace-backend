from flask import g
from ..common.exceptions import YouAreNotAllowedToView
from ..models.items import Communication, Event, Poll
from .common_functions import get_entity


def is_user_allowed_to_view_communication(communication_id):
    is_allowed_to_view = False
    communication = get_entity(communication_id, Communication)
    for organizationgroup in communication.organizationgroups.all():
        if g.current_user in organizationgroup.users.all():
            is_allowed_to_view = True
    if g.current_user.role == "admin":
        is_allowed_to_view = True
    if not is_allowed_to_view:
        msg = f"You are not allowed to view this communication "
        f"with id `{communication_id}`"
        raise YouAreNotAllowedToView(message=msg)


def is_user_allowed_to_view_event(event_id):
    is_allowed_to_view = False
    event = get_entity(event_id, Event)
    for organizationgroup in event.organizationgroups.all():
        if g.current_user in organizationgroup.users.all():
            is_allowed_to_view = True
    if g.current_user.role == "admin":
        is_allowed_to_view = True
    if not is_allowed_to_view:
        msg = f"You are not allowed to view this event "
        f"with id `{event_id}`"
        raise YouAreNotAllowedToView(message=msg)


def is_user_allowed_to_view_poll(poll_id):
    is_allowed_to_view = False
    poll = get_entity(poll_id, Poll)
    for organizationgroup in poll.organizationgroups.all():
        if g.current_user in organizationgroup.users.all():
            is_allowed_to_view = True
    if g.current_user.role == "admin":
        is_allowed_to_view = True
    if not is_allowed_to_view:
        msg = f"You are not allowed to view this poll "
        f"with id `{poll_id}`"
        raise YouAreNotAllowedToView(message=msg)
