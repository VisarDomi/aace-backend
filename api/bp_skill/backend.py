from flask import g
from ..common.models import Skill
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotDeleteOthersSkill,
)
from ..bp_user.backend import get_user_by_id


def create_skill(skill_data, user_id):
    if int(user_id) == g.current_user.id:
        skill = Skill(**skill_data)
        skill.user = g.current_user
        skill.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return skill


def get_skill_by_id(skill_id):
    try:
        skill = Skill.query.filter(Skill.id == skill_id).one()
    except NoResultFound:
        msg = f"There is no skill with id {skill_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {skill_id}`"
        raise InvalidURL(message=msg)
    return skill


def get_all_skills(user_id):
    skills = Skill.query.filter(Skill.user_id == user_id).all()
    return skills


def update_skill(skill_data, user_id, skill_id):
    if int(user_id) == g.current_user.id:
        skill = get_skill_by_id(skill_id)
        skill.update(**skill_data)
        skill.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return skill


def delete_skill(user_id, skill_id):
    user = get_user_by_id(user_id)
    skill = get_skill_by_id(skill_id)
    if user.email == g.current_user.email:
        skill.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersSkill(message=msg)
