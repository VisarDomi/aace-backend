from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaExperience
from ..common.exceptions import CannotDeleteOthersMedia, CannotGetOthersMedia
import os
from ..helper_functions.get_by_id import (
    get_experience_by_id,
    get_experience_media_by_id,
)


files_experience = UploadSet(
    name="experiencefiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def create_medias(media_data, user_id, experience_id):
    medias = []
    if int(user_id) == g.current_user.id:
        if get_experience_by_id(experience_id):
            for file in media_data:
                filename = files_experience.save(file)
                url = files_experience.url(filename)
                media = MediaExperience(filename=filename, url=url)
                experience = get_experience_by_id(experience_id)
                media.experience = experience
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_all_medias(user_id, experience_id):
    if int(user_id) == g.current_user.id or g.current_user.role == "admin":
        medias = MediaExperience.query.filter(
            MediaExperience.experience_id == int(experience_id)
        ).all()
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def update_media(media_data, user_id, experience_id, media_experience_id):
    if int(user_id) == g.current_user.id:
        medias = []
        media = MediaExperience.query.filter(
            MediaExperience.id == media_experience_id
        ).one_or_none()
        for file in media_data:
            if file and media:
                delete_media(user_id, media_experience_id)
                filename = files_experience.save(file)
                url = files_experience.url(filename)
                media = MediaExperience(filename=filename, url=url)
                experience = get_experience_by_id(experience_id)
                media.experience = experience
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/experience"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


def delete_media(user_id, media_experience_id):
    if int(user_id) == g.current_user.id:
        media = get_experience_media_by_id(user_id, media_experience_id)
        file_name = files_experience.path(media.filename)
        if is_file(media.filename):
            os.remove(get_file_path(file_name))
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersMedia(message=msg)
