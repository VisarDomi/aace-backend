from flask import g
from ..models.items import Experience
from ..common.exceptions import CannotChangeOthersProfile, CannotDeleteOthersExperience
from ..bp_media_experience.backend import delete_media, get_medias
from ..helper_functions.get_by_id import get_experience_by_id


def create_experience(experience_data, user_id):
    if int(user_id) == g.current_user.id:
        experience = Experience(**experience_data)
        experience.user = g.current_user
        experience.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return experience


def get_experiences(user_id):
    experiences = Experience.query.filter(Experience.user_id == user_id).all()

    return experiences


def update_experience(experience_data, user_id, experience_id):
    if int(user_id) == g.current_user.id:
        experience = get_experience_by_id(experience_id)
        experience.update(**experience_data)
        experience.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return experience


def delete_experience(user_id, experience_id):

    if int(user_id) == g.current_user.id:

        medias = get_medias(user_id, experience_id)
        for media in medias:
            delete_media(user_id, media.id)
        experience = get_experience_by_id(experience_id)
        experience.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersExperience(message=msg)
