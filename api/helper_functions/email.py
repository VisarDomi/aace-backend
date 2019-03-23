from threading import Thread
from flask import current_app
from flask_mail import Message
from config import Config
from .get_by_id import get_officialcommunication_by_id, get_user_by_id
from ..common.exceptions import EmailCannotBeSent
from ..common.extensions import mail


def send_async_email(api, msg):
    with api.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    Thread(
        target=send_async_email, args=(current_app._get_current_object(), msg)
    ).start()


def send_email_to_users(officialcommunication_id):
    officialcommunication = get_officialcommunication_by_id(officialcommunication_id)
    email_subject = officialcommunication.name
    email_sender = Config.MAIL_USERNAME
    email_recipients = []
    organizationgroups = officialcommunication.organizationgroups.all()
    for organizationgroup in organizationgroups:
        for user in organizationgroup.users.all():
            email_recipients.append(user.email)
    link = Config.WEBSITE
    link = ""
    email_text_body = (f"{officialcommunication.description}\n\n{officialcommunication.body}\n\n"
    "--------\n"
    "Komunikimi zyrtar nga SHOSHIK\n"
    "Filan Fisteku, Sekretar i pergjithshem\n"
    "Rruga Qofte e Mbushur, 200L\n""Website: www.aace.al\n"
    "Telefon: +093802304234\n"
    "Email: info@aace.al"
    )
    if email_subject and email_sender and email_recipients and email_text_body:
        send_email(
            subject=email_subject,
            sender=email_sender,
            recipients=email_recipients,
            text_body=email_text_body,
        )
    else:
        msg = (
            "There is missing arguments: email_subject, email_sender, "
            "email_recipients, email_text_body"
        )
        raise EmailCannotBeSent(message=msg)


def send_email_to_user(email_data, user_id):
    try:
        user = get_user_by_id(user_id)
        email_subject = email_data["subject"]
        email_sender = Config.MAIL_USERNAME
        email_recipients = []
        email_recipients.append(user.email)
        link = Config.WEBSITE
        link = ""
        email_text_body = email_data["text_body"] + "\n" + link
        if email_subject and email_sender and email_recipients and email_text_body:
            send_email(
                subject=email_subject,
                sender=email_sender,
                recipients=email_recipients,
                text_body=email_text_body,
            )
        else:
            msg = (
                "There is missing arguments: email_subject, email_sender, "
                "email_recipients, email_text_body"
            )
            raise EmailCannotBeSent(message=msg)
    except ValueError:
        msg = "You didn't send strings on fields subject and text_body."
        raise EmailCannotBeSent(message=msg)
