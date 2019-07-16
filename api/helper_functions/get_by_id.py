from ..models.users import User
from ..models.items import (
    Education,
    Experience,
    Skill,
    Payment,
    OrganizationGroup,
    Communication,
    Event,
    Poll,
    Comment,
    Option,
    ContactForm,
)
from .is_allowed import (
    is_user_allowed_to_view_communication,
    is_user_allowed_to_view_event,
    is_user_allowed_to_view_poll,
)
from .common_functions import get_entity


def get_user_by_id(user_id):
    user = get_entity(user_id, User)

    return user


def get_education_by_id(education_id):
    education = get_entity(education_id, Education)

    return education


def get_experience_by_id(experience_id):
    experience = get_entity(experience_id, Experience)

    return experience


def get_skill_by_id(skill_id):
    skill = get_entity(skill_id, Skill)

    return skill


def get_payment_by_id(payment_id):
    payment = get_entity(payment_id, Payment)

    return payment


def get_comment_by_id(comment_id):
    comment = get_entity(comment_id, Comment)

    return comment


def get_option_by_id(poll_id, option_id):
    option = get_entity(option_id, Option)
    is_user_allowed_to_view_poll(poll_id)

    return option


def get_communication_by_id(communication_id):
    communication = get_entity(communication_id, Communication)
    is_user_allowed_to_view_communication(communication_id)

    return communication


def get_event_by_id(event_id):
    event = get_entity(event_id, Event)
    is_user_allowed_to_view_event(event_id)

    return event


def get_poll_by_id(poll_id):
    poll = get_entity(poll_id, Poll)
    is_user_allowed_to_view_poll(poll_id)

    return poll


def get_organizationgroup_by_id(organizationgroup_id):
    organizationgroup = get_entity(organizationgroup_id, OrganizationGroup)

    return organizationgroup


def get_contactform_by_id(contactform_id):
    contactform = get_entity(contactform_id, ContactForm)

    return contactform
