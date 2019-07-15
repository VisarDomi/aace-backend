from flask import g
from ..models.items import Skill
from ..common.exceptions import CannotChangeOthersProfile, CannotDeleteOthersSkill
from ..bp_media_skill.backend import delete_media, get_medias
from ..helper_functions.get_by_id import get_skill_by_id


def create_skill(skill_data, user_id):
    if int(user_id) == g.current_user.id:
        skill = Skill(**skill_data)
        skill.user = g.current_user
        skill.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)

    return skill


def get_skills(user_id):
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

    if int(user_id) == g.current_user.id:

        medias = get_medias(user_id, skill_id)
        for media in medias:
            delete_media(user_id, media.id)
        skill = get_skill_by_id(skill_id)
        skill.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersSkill(message=msg)
