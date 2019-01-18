from flask import g
from ..common.models import Event
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL


def create_event(event_data):
    event = Event.new_from_dict(event_data)
    event.user = g.current_user
    event.save()
    return event


def get_event_by_id(event_id):
    try:
        result = Event.query.filter(Event.id == event_id).one()
    except NoResultFound:
        msg = f'There is no event with id {event_id}'
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {event_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_events():
    events = Event.query.all()
    return events


def update_event(event_data, event_id):
    event = get_event_by_id(event_id)
    event.update_from_dict(event_data)
    event.save()
    return event


def delete_event(event_id):
    event = get_event_by_id(event_id)
    event.delete()
