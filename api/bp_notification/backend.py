from flask import g
from ..common.models import Notification
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotNotificationOnOthersProfile,
)


def create_notification(notification_data, user_id):
    if int(user_id) == g.current_user.id:
        notification = Notification.new_from_dict(notification_data)
        notification.user = g.current_user
        notification.save()
    else:
        msg = f"You can't notification on other people's profile."
        raise CannotNotificationOnOthersProfile(message=msg)
    return notification


def get_notification_by_id(notification_id):
    try:
        result = Notification.query.filter(Notification.id == notification_id).one()
    except NoResultFound:
        msg = f"There is no notification with id {notification_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {notification_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_notifications(user_id):
    notifications = Notification.query.filter(
        Notification.user_id == int(user_id)
    ).all()
    return notifications


def update_notification(notification_data, user_id, notification_id):
    if int(user_id) == g.current_user.id:
        notification = get_notification_by_id(notification_id)
        notification.update_from_dict(notification_data)
        notification.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return notification


def delete_notification(notification_id):
    notification = get_notification_by_id(notification_id)
    notification.delete()
