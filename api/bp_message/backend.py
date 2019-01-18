from flask import g
from ..common.models import Message
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL


def create_message(message_data):
    message = Message.new_from_dict(message_data)
    message.user = g.current_user
    message.save()
    return message


def get_message_by_id(message_id):
    try:
        result = Message.query.filter(Message.id == message_id).one()
    except NoResultFound:
        msg = f'There is no message with id {message_id}'
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {message_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_messages():
    messages = Message.query.all()
    return messages


def update_message(message_data, message_id):
    message = get_message_by_id(message_id)
    message.update_from_dict(message_data)
    message.save()
    return message


def delete_message(message_id):
    message = get_message_by_id(message_id)
    message.delete()
