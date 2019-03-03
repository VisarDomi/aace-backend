from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import MediaUser, User
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    CannotDeleteOthersMedia,
    InvalidURL,
    CannotGetOthersMedia,
)
import os


files_user = UploadSet(name="userfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES))


def get_user_by_id(user_id):
    try:
        user = User.query.filter(User.id == user_id).one()
    except NoResultFound:
        msg = f"There is no User with `id: {user_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {user_id}`"
        raise InvalidURL(message=msg)

    return user


def user_edited(user_id):
    user = get_user_by_id(user_id)
    if user.register_status not in ["applying", "reapplying"]:
        user.register_status = "reapplying"
    user.save()


def create_medias(media_data, user_id):
    medias = []
    if int(user_id) == g.current_user.id:
        for file in media_data:
            media_filename = files_user.save(file)
            media_url = files_user.url(media_filename)
            media = MediaUser(media_filename=media_filename, media_url=media_url)
            media.user = g.current_user
            media.save()
            medias.append(media)
            user_edited(user_id)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_media_by_id(user_id, media_user_id):
    if int(user_id) == g.current_user.id:
        try:
            media = MediaUser.query.filter(MediaUser.id == media_user_id).one()
        except NoResultFound:
            msg = f"There is no media with id {media_user_id}"
            raise RecordNotFound(message=msg)
        except InvalidURL:
            msg = f"This is not a valid URL: {media_user_id}`"
            raise InvalidURL(message=msg)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return media


def get_all_medias(user_id):
    if int(user_id) == g.current_user.id:
        medias = MediaUser.query.filter(MediaUser.user_id == int(user_id)).all()
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def update_media(media_data, user_id, media_user_id):
    if int(user_id) == g.current_user.id:
        medias = []
        media = MediaUser.query.filter(MediaUser.id == media_user_id).one_or_none()
        for file in media_data:
            if file and media:
                delete_media(user_id, media_user_id)
                media_filename = files_user.save(file)
                media_url = files_user.url(media_filename)
                media = MediaUser(media_filename=media_filename, media_url=media_url)
                media.user = g.current_user
                media.save()
                medias.append(media)
                user_edited(user_id)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/user"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


def delete_media(user_id, media_user_id):
    if int(user_id) == g.current_user.id:
        media = get_media_by_id(user_id, media_user_id)
        file_name = files_user.path(media.media_filename)
        if is_file(media.media_filename):
            os.remove(get_file_path(file_name))
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersMedia(message=msg)
