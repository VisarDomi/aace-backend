from . import backend
import json


def create_message(message_data):
    message = backend.create_message(message_data)
    return message.to_json(max_nesting=2)


def get_message_by_id(message_id):
    message = backend.get_message_by_id(message_id)
    message_json = message.to_json(max_nesting=2)
    return message_json


def get_all_messages():
    messages = backend.get_all_messages()
    list_of_messages = [
        message.to_dict(max_nesting=2) for message in messages
    ]
    json_dump_of_list_of_messages = json.dumps(list_of_messages, default=str)
    return json_dump_of_list_of_messages


def update_message(message_data, message_id):
    message = backend.update_message(message_data, message_id)
    return message.to_json(max_nesting=2)


def delete_message(message_id):
    backend.delete_message(message_id)
