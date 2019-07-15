from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaEducation
from ..common.exceptions import CannotDeleteOthersMedia, CannotGetOthersMedia
import os
from ..helper_functions.get_by_id import get_education_by_id
from ..helper_functions.get_media_by_id import get_education_media_by_id


files_education = UploadSet(
    name="educationfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def create_medias(media_data, user_id, education_id):
    if int(user_id) == g.current_user.id:
        medias = []
        if get_education_by_id(education_id):
            for file in media_data:
                filename = files_education.save(file)
                url = files_education.url(filename)
                media = MediaEducation(filename=filename, url=url)
                education = get_education_by_id(education_id)
                media.education = education
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_medias(user_id, education_id):
    if int(user_id) == g.current_user.id or g.current_user.role == "admin":
        medias = MediaEducation.query.filter(
            MediaEducation.education_id == int(education_id)
        ).all()
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def update_media(media_data, user_id, education_id, media_education_id):
    if int(user_id) == g.current_user.id:
        medias = []
        media = MediaEducation.query.filter(
            MediaEducation.id == media_education_id
        ).one_or_none()
        for file in media_data:
            if file and media:
                delete_media(user_id, media_education_id)
                filename = files_education.save(file)
                url = files_education.url(filename)
                media = MediaEducation(filename=filename, url=url)
                education = get_education_by_id(education_id)
                media.education = education
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/education"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


def delete_media(user_id, media_education_id):
    if int(user_id) == g.current_user.id:
        media = get_education_media_by_id(user_id, media_education_id)
        file_name = files_education.path(media.filename)
        if is_file(media.filename):
            os.remove(get_file_path(file_name))
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersMedia(message=msg)
