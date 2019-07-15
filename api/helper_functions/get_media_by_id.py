from ..models.medias import (
    MediaUser,
    MediaEducation,
    MediaExperience,
    MediaSkill,
    MediaPayment,
    MediaOrganizationGroup,
    MediaCommunication,
    MediaEvent,
    MediaPoll,
    MediaComment,
)
from .common_functions import get_entity, same_user_get_media


def get_user_media_by_id(media_user_id):
    user_media = get_entity(media_user_id, MediaUser)

    return user_media


def get_education_media_by_id(user_id, media_education_id):
    education_media = same_user_get_media(user_id, media_education_id, MediaEducation)

    return education_media


def get_experience_media_by_id(user_id, media_experience_id):
    experience_media = same_user_get_media(
        user_id, media_experience_id, MediaExperience
    )

    return experience_media


def get_skill_media_by_id(user_id, media_skill_id):
    skill_media = same_user_get_media(user_id, media_skill_id, MediaSkill)

    return skill_media


def get_payment_media_by_id(user_id, media_payment_id):
    payment_media = same_user_get_media(user_id, media_payment_id, MediaPayment)

    return payment_media


def get_organizationgroup_media_by_id(media_organizationgroup_id):
    organizationgroup_media = get_entity(
        media_organizationgroup_id, MediaOrganizationGroup
    )

    return organizationgroup_media


def get_communication_media_by_id(media_communication_id):
    communication_media = get_entity(media_communication_id, MediaCommunication)

    return communication_media


def get_event_media_by_id(media_event_id):
    event_media = get_entity(media_event_id, MediaEvent)

    return event_media


def get_poll_media_by_id(media_poll_id):
    poll_media = get_entity(media_poll_id, MediaPoll)

    return poll_media


def get_comment_media_by_id(media_comment_id):
    comment_media = get_entity(media_comment_id, MediaComment)

    return comment_media
