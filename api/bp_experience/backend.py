from flask import g
from ..common.models import Experience
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL, CannotChangeOthersProfile


def create_experience(experience_data, user_id):
    if user_id != g.current_user.id:
        experience = Experience.new_from_dict(experience_data)
        experience.user = g.current_user
        experience.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return experience


def get_experience_by_id(experience_id):
    try:
        result = Experience.query.filter(Experience.id == experience_id).one()
    except NoResultFound:
        msg = f"There is no experience with id {experience_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {experience_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_experiences(user_id):
    experiences = Experience.query.filter(Experience.user_id == user_id).all()
    return experiences


def update_experience(experience_data, user_id, experience_id):
    if user_id != g.current_user.id:
        experience = get_experience_by_id(experience_id)
        experience.update_from_dict(experience_data)
        experience.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return experience


def delete_experience(experience_id):
    experience = get_experience_by_id(experience_id)
    experience.delete()
