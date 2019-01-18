from flask import g
from ..common.models import Event
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotEventOnOthersProfile,
)


def create_post(post_data, user_id):
    if int(user_id) == g.current_user.id:
        post = Event.new_from_dict(post_data)
        post.user = g.current_user
        post.save()
    else:
        msg = f"You can't post on other people's profile."
        raise CannotEventOnOthersProfile(message=msg)
    return post


def get_post_by_id(post_id):
    try:
        result = Event.query.filter(Event.id == post_id).one()
    except NoResultFound:
        msg = f"There is no post with id {post_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {post_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_posts(user_id):
    posts = Event.query.filter(Event.user_id == int(user_id)).all()
    return posts


def update_post(post_data, user_id, post_id):
    if int(user_id) == g.current_user.id:
        post = get_post_by_id(post_id)
        post.update_from_dict(post_data)
        post.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return post


def delete_post(post_id):
    post = get_post_by_id(post_id)
    post.delete()
