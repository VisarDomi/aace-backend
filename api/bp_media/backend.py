from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import Media
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    CannotDeleteOthersPost,
    InvalidURL,
    CannotChangeOthersProfile,
)
import os
from ..bp_user.backend import get_user_by_id

files = UploadSet("files", AllExcept(SCRIPTS + EXECUTABLES))


def create_media(
    media_data,
    user_id,
    accomplishment_id,
    comment_id,
    event_id,
    education_id,
    experience_id,
    message_id,
    post_id,
):
    medias = []
    if int(user_id) == g.current_user.id:
        for file in media_data:
            media_filename = files.save(file)
            media_url = files.url(media_filename)
            media = Media(media_filename=media_filename, media_url=media_url)
            if comment_id:
                media.comment = g.current_user.comments.filter_by(
                    id=int(comment_id)
                ).one()
            elif event_id:
                media.event = g.current_user.events.filter_by(id=int(event_id)).one()
            elif experience_id:
                media.experience = g.current_user.experiences.filter_by(
                    id=int(experience_id)
                ).one()
            elif message_id:
                media.message = g.current_user.messages.filter_by(
                    id=int(message_id)
                ).one()
            elif post_id:
                media.post = g.current_user.posts.filter_by(id=int(post_id)).one()
            media.save()
            medias.append(media)
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return medias


def get_media_by_id(media_id):
    try:
        result = Media.query.filter(Media.id == media_id).one()
    except NoResultFound:
        msg = f"There is no media with id {media_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_medias(comment_id, event_id, experience_id, message_id, post_id):
    if comment_id:
        medias = Media.query.filter(Media.comment_id == int(comment_id)).all()
    if event_id:
        medias = Media.query.filter(Media.event_id == int(event_id)).all()
    if experience_id:
        medias = Media.query.filter(Media.experience_id == int(experience_id)).all()
    if message_id:
        medias = Media.query.filter(Media.message_id == int(message_id)).all()
    if post_id:
        medias = Media.query.filter(Media.post_id == int(post_id)).all()

    return medias


def update_media(media_data, user_id, media_id):
    if int(user_id) == g.current_user.id:
        media = get_media_by_id(media_id)
        media.update_from_dict(media_data)
        media.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return media


def delete_media(user_id, media_id):
    user = get_user_by_id(user_id)
    media = get_media_by_id(media_id)
    if user.email == g.current_user.email:
        file_path = files.path(media.media_filename)
        os.remove(file_path)
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersPost(message=msg)
