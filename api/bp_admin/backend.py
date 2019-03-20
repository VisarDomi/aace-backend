from ..common.exceptions import CannotChangeFirstAdminProperties
from ..common.models import User
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_user_by_id
from ..helper_functions.email import send_email_to_user


def get_application_status_users(application_status):
    users = User.query.filter(User.application_status == application_status).all()

    return users


def get_payment_status_users(payment_status):
    users = User.query.filter(User.payment_status == payment_status).all()

    return users


@admin_required
def get_blank_users():
    users = get_application_status_users("blank")

    return users


@admin_required
def get_rejected_users():
    users = get_application_status_users("rejected")

    return users


@admin_required
def get_accepted_users():
    users = get_application_status_users("accepted")

    return users


@admin_required
def get_applying_and_reapplying_users():
    users = User.query.filter(
        (User.register_status == "applying") | (User.register_status == "reapplying")
    ).all()
    return users


@admin_required
def get_applying_users():
    users = get_application_status_users("applying")

    return users


@admin_required
def get_reapplying_users():
    users = get_application_status_users("reapplying")

    return users


@admin_required
def get_rebutted_users():
    users = get_application_status_users("rebutted")

    return users


@admin_required
def get_accepted_application_users():
    users = get_application_status_users("accepted_application")

    return users


@admin_required
def get_rebutted_payment_users():
    users = get_payment_status_users("rebutted_payment")

    return users


@admin_required
def get_accepted_payment_users():
    users = get_payment_status_users("accepted_payment")

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
