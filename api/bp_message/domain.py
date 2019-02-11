from . import backend
import json


def create_message(message_data, user_id):
    message = backend.create_message(message_data, user_id)
    return message.to_json(max_nesting=1)


def get_message_by_id(message_id):
    message = backend.get_message_by_id(message_id)
    message_json = message.to_json(max_nesting=1)
    return message_json


def get_all_messages(user_id):
    messages = backend.get_all_messages(user_id)
    list_of_messages = [
        message.to_dict(max_nesting=1) for message in messages
    ]
    json_dump_of_list_of_messages = json.dumps(list_of_messages, default=str)
    return json_dump_of_list_of_messages


def update_message(message_data, user_id, message_id):
    message = backend.update_message(message_data, user_id, message_id)
    return message.to_json(max_nesting=1)


def delete_message(message_id):
    backend.delete_message(message_id)
