from . import backend
import json


def create_event(event_data, user_id):
    event = backend.create_event(event_data, user_id)
    return event.to_json(max_nesting=2)


def get_event_by_id(event_id):
    event = backend.get_event_by_id(event_id)
    event_json = event.to_json(max_nesting=2)
    return event_json


def get_all_events(user_id):
    events = backend.get_all_events(user_id)
    list_of_events = [
        event.to_dict(max_nesting=2) for event in events
    ]
    json_dump_of_list_of_events = json.dumps(list_of_events, default=str)
    return json_dump_of_list_of_events


def update_event(event_data, user_id, event_id):
    event = backend.update_event(event_data, user_id, event_id)
    return event.to_json(max_nesting=2)


def delete_event(event_id):
    backend.delete_event(event_id)
