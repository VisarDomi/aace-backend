from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaUser
from ..common.exceptions import CannotDeleteOthersMedia, CannotGetOthersMedia
import os
from ..helper_functions.get_by_id import get_user_media_by_id


files_user = UploadSet(name="userfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES))


def create_medias(media_data, user_id):
    medias = []
    if int(user_id) == g.current_user.id:
        for file in media_data:
            filename = files_user.save(file)
            url = files_user.url(filename)
            media = MediaUser(filename=filename, url=url)
            media.user = g.current_user
            media.save()
            medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_all_medias(user_id):
    medias = MediaUser.query.filter(MediaUser.user_id == int(user_id)).all()

    return medias


def update_media(media_data, user_id, media_user_id):
    if int(user_id) == g.current_user.id:
        medias = []
        media = MediaUser.query.filter(MediaUser.id == media_user_id).one_or_none()
        for file in media_data:
            if file and media:
                delete_media(user_id, media_user_id)
                filename = files_user.save(file)
                url = files_user.url(filename)
                media = MediaUser(filename=filename, url=url)
                media.user = g.current_user
                media.save()
                medias.append(media)
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
        media = get_user_media_by_id(media_user_id)
        file_name = files_user.path(media.filename)
        if is_file(media.filename):
            os.remove(get_file_path(file_name))
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersMedia(message=msg)
