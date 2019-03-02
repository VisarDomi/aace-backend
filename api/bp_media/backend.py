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

FILES = UploadSet("files", AllExcept(SCRIPTS + EXECUTABLES))


def create_media(
    media_data,
    user_id,
    skill_id,
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
            media_filename = FILES.save(file)
            media_url = FILES.url(media_filename)
            media = Media(media_filename=media_filename, media_url=media_url)
            if skill_id:
                media.skill = g.current_user.skills.filter_by(id=int(skill_id)).one()
            elif comment_id:
                media.comment = g.current_user.comments.filter_by(
                    id=int(comment_id)
                ).one()
            elif education_id:
                media.education = g.current_user.educations.filter_by(
                    id=int(education_id)
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
            else:
                media.user = g.current_user
            media.save()
            medias.append(media)
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return medias


def get_media_by_id(media_id):
    try:
        media = Media.query.filter(Media.id == media_id).one()
    except NoResultFound:
        msg = f"There is no media with id {media_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_id}`"
        raise InvalidURL(message=msg)
    return media


def get_all_medias(
    user_id,
    skill_id,
    comment_id,
    education_id,
    event_id,
    experience_id,
    message_id,
    post_id,
):
    if skill_id:
        medias = Media.query.filter(Media.skill_id == int(skill_id)).all()
    elif comment_id:
        medias = Media.query.filter(Media.comment_id == int(comment_id)).all()
    elif event_id:
        medias = Media.query.filter(Media.event_id == int(event_id)).all()
    elif education_id:
        medias = Media.query.filter(Media.education_id == int(education_id)).all()
    elif experience_id:
        medias = Media.query.filter(Media.experience_id == int(experience_id)).all()
    elif message_id:
        medias = Media.query.filter(Media.message_id == int(message_id)).all()
    elif post_id:
        medias = Media.query.filter(Media.post_id == int(post_id)).all()
    else:
        medias = Media.query.filter(Media.user_id == int(user_id)).all()

    return medias


def update_media(
    media_data,
    user_id,
    media_id,
    skill_id,
    comment_id,
    event_id,
    education_id,
    experience_id,
    message_id,
    post_id,
):
    if int(user_id) == g.current_user.id:
        medias = []
        media = Media.query.filter(Media.id == media_id).one_or_none()

        for file in media_data:
            if file and media:
                delete_media_user(user_id, media_id)

                media_filename = FILES.save(file)
                media_url = FILES.url(media_filename)
                media = Media(media_filename=media_filename, media_url=media_url)

                if skill_id:
                    media.skill = g.current_user.skills.filter_by(
                        id=int(skill_id)
                    ).one()
                elif comment_id:
                    media.comment = g.current_user.comments.filter_by(
                        id=int(comment_id)
                    ).one()
                elif education_id:
                    media.education = g.current_user.educations.filter_by(
                        id=int(education_id)
                    ).one()
                elif event_id:
                    media.event = g.current_user.events.filter_by(
                        id=int(event_id)
                    ).one()
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
                else:
                    media.user = g.current_user

                media.save()
                medias.append(media)
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return medias


def get_file_path(file_name):
    PARENT_DIR = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files"
    FILE_PATH = os.path.join(PARENT_DIR, FILE_TO_PATH)
    F_PATH = os.path.join(FILE_PATH, file_name)
    return F_PATH


def is_file(file_name):
    THIS_FILE_PATH = get_file_path(file_name)
    return os.path.exists(THIS_FILE_PATH)


def delete_media_user(user_id, media_id):
    media = get_media_by_id(media_id)
    if int(user_id) == g.current_user.id:
        file_name = FILES.path(media.media_filename)

        if is_file(media.media_filename):
            print("os.remove(get_file_path(file_name)) :", file_name)
            os.remove(get_file_path(file_name))
        print("media.delete() :", media)
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersPost(message=msg)


def delete_media_education(user_id, education_id, media_id):
    media = get_media_by_id(media_id)
    if int(user_id) == g.current_user.id:
        file_name = FILES.path(media.media_filename)

        if is_file(media.media_filename):
            print("os.remove(get_file_path(file_name)) :", file_name)
            os.remove(get_file_path(file_name))
        print("media.delete() :", media)
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersPost(message=msg)
