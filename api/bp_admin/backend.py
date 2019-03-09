from ..common.exceptions import CannotChangeFirstAdminProperties
from ..common.models import User
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_user_by_id
from ..helper_functions.email import send_email_to_user


def get_register_status_users(register_status):
    users = User.query.filter(User.register_status == register_status).all()

    return users


@admin_required
def get_approved_users():
    users = get_register_status_users("approved")

    return users


@admin_required
def get_applying_users():
    users = get_register_status_users("applying")

    return users


@admin_required
def get_applying_and_reapplying_users():
    users = User.query.filter(
        (User.register_status == "applying") | (User.register_status == "reapplying")
    ).all()
    return users


@admin_required
def get_rejected_users():
    users = get_register_status_users("rejected")

    return users


@admin_required
def get_rebutted_users():
    users = get_register_status_users("rebutted")

    return users


@admin_required
def get_reapplying_users():
    users = get_register_status_users("reapplying")

    return users


@admin_required
def get_blank_users():
    users = get_register_status_users("blank")

    return users


def get_and_update_user(user_data, user_id):
    user = get_user_by_id(user_id)
    user.update(**user_data)
    user.save()

    return user


@admin_required
def update_user(user_data, user_id):

    secure = True
    if secure:
        if int(user_id) != 1:
            user = get_and_update_user(user_data, user_id)
        else:
            msg = "Cannot change admin with `id: %s`" % user_id
            raise CannotChangeFirstAdminProperties(message=msg)
    else:
        user = get_and_update_user(user_data, user_id)

    return user


@admin_required
def send_email(email_data, user_id):
    send_email_to_user(email_data, user_id)
