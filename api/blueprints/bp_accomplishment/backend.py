from flask import g
from ...common.models import Accomplishment
from sqlalchemy.orm.exc import NoResultFound
from ...common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotDeleteOthersAccomplishment,
)
from ..bp_user.backend import get_user_by_id


def create_accomplishment(accomplishment_data, user_id):
    if int(user_id) == g.current_user.id:
        accomplishment = Accomplishment.new_from_dict(accomplishment_data)
        accomplishment.user = g.current_user
        accomplishment.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return accomplishment


def get_accomplishment_by_id(accomplishment_id):
    try:
        result = Accomplishment.query.filter(
            Accomplishment.id == accomplishment_id
        ).one()
    except NoResultFound:
        msg = f"There is no accomplishment with id {accomplishment_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {accomplishment_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_accomplishments(user_id):
    accomplishments = Accomplishment.query.filter(
        Accomplishment.user_id == user_id
    ).all()
    return accomplishments


def update_accomplishment(accomplishment_data, user_id, accomplishment_id):
    if int(user_id) == g.current_user.id:
        accomplishment = get_accomplishment_by_id(accomplishment_id)
        accomplishment.update_from_dict(accomplishment_data)
        accomplishment.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return accomplishment


def delete_accomplishment(user_id, accomplishment_id):
    user = get_user_by_id(user_id)
    accomplishment = get_accomplishment_by_id(accomplishment_id)
    if user.email == g.current_user.email:
        accomplishment.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersAccomplishment(message=msg)
