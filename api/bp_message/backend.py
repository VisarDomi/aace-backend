from flask import g
from ..common.models import Message
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotMessageOnOthersProfile,
)


def create_message(message_data, user_id):
    if int(user_id) == g.current_user.id:
        message = Message.new_from_dict(message_data)
        message.user = g.current_user
        message.save()
    else:
        msg = f"You can't message on other people's profile."
        raise CannotMessageOnOthersProfile(message=msg)
    return message


def get_message_by_id(message_id):
    try:
        result = Message.query.filter(Message.id == message_id).one()
    except NoResultFound:
        msg = f"There is no message with id {message_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {message_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_messages(user_id):
    messages = Message.query.filter(Message.user_id == int(user_id)).all()
    return messages


def update_message(message_data, user_id, message_id):
    if int(user_id) == g.current_user.id:
        message = get_message_by_id(message_id)
        message.update_from_dict(message_data)
        message.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return message


def delete_message(message_id):
    message = get_message_by_id(message_id)
    message.delete()
