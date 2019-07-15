from . import backend
from ..helper_functions.get_by_id import get_event_by_id


def create_event(event_data):
    event = backend.create_event(event_data)
    event_dict = event.to_dict()

    return event_dict


def get_events():
    events = backend.get_events()
    events_list = [event.to_dict() for event in events]

    return events_list


def get_event(event_id):
    event = get_event_by_id(event_id)
    event_dict = event.to_dict()

    event_medias = []
    for event_media in event.medias:
        event_medias.append(event_media.to_dict())
    event_dict["event_medias"] = event_medias

    return event_dict


def update_event(event_data, event_id):
    event = backend.update_event(event_data, event_id)
    event_dict = event.to_dict()

    return event_dict


def delete_event(event_id):
    backend.delete_event(event_id)


def get_organizationgroups_from_event(event_id):
    organizationgroups = backend.get_organizationgroups_from_event(event_id)

    organizationgroups_list = [
        organizationgroup.to_dict() for organizationgroup in organizationgroups
    ]

    return organizationgroups_list


def add_organizationgroup_to_event(event_id, organizationgroup_id):
    event = backend.add_organizationgroup_to_event(event_id, organizationgroup_id)
    event_dict = event.to_dict()

    return event_dict


def remove_organizationgroup_from_event(event_id, organizationgroup_id):
    backend.remove_organizationgroup_from_event(event_id, organizationgroup_id)


def send_email(event_id):
    backend.send_email(event_id)
