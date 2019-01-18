from flask import g
from ..common.models import Notification
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL


def create_notification(notification_data):
    notification = Notification.new_from_dict(notification_data)
    notification.user = g.current_user
    notification.save()
    return notification


def get_notification_by_id(notification_id):
    try:
        result = Notification.query.filter(Notification.id == notification_id).one()
    except NoResultFound:
        msg = f'There is no notification with id {notification_id}'
        raise RecordNotFound(notification=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {notification_id}`"
        raise InvalidURL(notification=msg)
    return result


def get_all_notifications():
    notifications = Notification.query.all()
    return notifications


def update_notification(notification_data, notification_id):
    notification = get_notification_by_id(notification_id)
    notification.update_from_dict(notification_data)
    notification.save()
    return notification


def delete_notification(notification_id):
    notification = get_notification_by_id(notification_id)
    notification.delete()
