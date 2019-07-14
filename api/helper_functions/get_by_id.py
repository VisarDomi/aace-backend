from flask import g
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    YouAreNotAllowedToView,
    CannotGetOthersMedia,
)
from ..common.models.users import User
from ..common.models.medias import (
    MediaUser,
    MediaEducation,
    MediaExperience,
    MediaSkill,
    MediaPayment,
    MediaOrganizationGroup,
    MediaCommunication,
    MediaComment,
)
from ..common.models.items import (
    Education,
    Experience,
    Skill,
    Payment,
    OrganizationGroup,
    Communication,
    Comment,
)


##############################################################
#                        Media                               #
##############################################################


def get_entity(entity_id, Entity):
    try:
        entity = Entity.query.filter(Entity.id == int(entity_id)).one()
    except NoResultFound:
        msg = f"There is no entity with id {entity_id}"
        raise RecordNotFound(message=msg)
    except (InvalidURL, ValueError):
        msg = f"This is not a valid URL: {entity_id}`"
        raise InvalidURL(message=msg)

    return entity


def same_user_get_media(user_id, media_id, Media):
    if int(user_id) == g.current_user.id or g.current_user.role == "admin":
        media = get_entity(media_id, Media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return media


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
    communication_media = get_entity(
        media_communication_id, MediaCommunication
    )

    return communication_media


def get_comment_media_by_id(media_comment_id):
    comment_media = get_entity(media_comment_id, MediaComment)

    return comment_media


##############################################################
#                        Non-Media                           #
##############################################################


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


def is_user_allowed_to_view(communication):
    is_allowed_to_view = False
    for organizationgroup in communication.organizationgroups.all():
        if g.current_user in organizationgroup.users.all():
            is_allowed_to_view = True
    if g.current_user.role == "admin":
        is_allowed_to_view = True
    if not is_allowed_to_view:
        msg = f"You are not allowed to view this communication "
        "with id `{comment_id}``"
        raise YouAreNotAllowedToView(message=msg)


def get_comment_by_id(communication_id, comment_id):
    comment = get_entity(comment_id, Comment)
    communication = get_communication_by_id(communication_id)
    is_user_allowed_to_view(communication)

    return comment


def get_communication_by_id(communication_id):
    communication = get_entity(communication_id, Communication)
    is_user_allowed_to_view(communication)

    return communication


def get_organizationgroup_by_id(organizationgroup_id):
    organizationgroup = get_entity(organizationgroup_id, OrganizationGroup)

    return organizationgroup
