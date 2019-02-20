from flask import g
from ...common.models import Event, Post
from sqlalchemy.orm.exc import NoResultFound
from ...common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotEventOnOthersProfile,
    PostIsAlreadyPartOfEvent,
    NoPostByThatID,
    CannotDeleteOthersPost,
)
from ..bp_post.backend import get_post_by_id
from ..bp_user.backend import get_user_by_id


def create_event(event_data, user_id):
    if int(user_id) == g.current_user.id:
        event = Event.new_from_dict(event_data)
        event.user = g.current_user
        event.save()
    else:
        msg = f"You can't event on other people's profile."
        raise CannotEventOnOthersProfile(message=msg)
    return event


def get_event_by_id(event_id):
    try:
        result = Event.query.filter(Event.id == event_id).one()
    except NoResultFound:
        msg = f"There is no event with id {event_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {event_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_events(user_id):
    events = Event.query.filter(Event.user_id == int(user_id)).all()
    return events


def update_event(event_data, user_id, event_id):
    if int(user_id) == g.current_user.id:
        event = get_event_by_id(event_id)
        event.update_from_dict(event_data)
        event.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return event


def delete_event(user_id, event_id):
    user = get_user_by_id(user_id)
    if user.email == g.current_user.email:
        user.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersPost(message=msg)


def create_post_to_event(post_data, user_id, event_id):
    if int(user_id) == g.current_user.id:
        event = get_event_by_id(event_id)
        post = Post.new_from_dict(post_data)
        event.posts.append(post)
        event.save()
    else:
        msg = f"You can't event on other people's profile."
        raise CannotEventOnOthersProfile(message=msg)
    return event


def get_posts_from_event(event_id):
    event = get_event_by_id(event_id)
    posts = event.posts.all()
    return posts


def get_post_from_event(post_id):
    post = get_post_by_id(post_id)
    return post


def update_post_to_event(post_data, user_id, event_id, post_id):
    if int(user_id) == g.current_user.id:
        event = get_event_by_id(event_id)
        post = get_post_by_id(post_id)
        post = post.update_from_dict(post_data)
        if post != event.posts.filter(Post.id == post_id).one_or_none():
            event.posts.append(post)
            event.save()
        else:
            msg = "Post % s is already part of the event % s." % (post_id, event_id)
            raise PostIsAlreadyPartOfEvent(message=msg)
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return event


def remove_post_from_event(user_id, event_id, post_id):

    event = get_event_by_id(event_id)
    post = event.posts.filter(Post.id == post_id).one_or_none()
    if post is not None:
        post = Post.query.filter(Post.id == post_id).one()
        event.posts.remove(post)
        event.save()
    else:
        msg = "Post with `id: %s` is not part of the event with `id %s`." % (
            post_id,
            event_id,
        )
        raise NoPostByThatID(message=msg)
