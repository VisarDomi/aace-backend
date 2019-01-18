from . import backend
import json


def create_notification(notification_data):
    notification = backend.create_notification(notification_data)
    return notification.to_json(max_nesting=2)


def get_notification_by_id(notification_id):
    notification = backend.get_notification_by_id(notification_id)
    notification_json = notification.to_json(max_nesting=2)
    return notification_json


def get_all_notifications():
    notifications = backend.get_all_notifications()
    list_of_notifications = [
        notification.to_dict(max_nesting=2) for notification in notifications
    ]
    json_dump_of_list_of_notifications = json.dumps(list_of_notifications, default=str)
    return json_dump_of_list_of_notifications


def update_notification(notification_data, notification_id):
    notification = backend.update_notification(notification_data, notification_id)
    return notification.to_json(max_nesting=2)


def delete_notification(notification_id):
    backend.delete_notification(notification_id)
