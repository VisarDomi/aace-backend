from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import MediaEducation, Education, User
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    CannotDeleteOthersMedia,
    InvalidURL,
    CannotGetOthersMedia,
)
import os


files_education = UploadSet(
    name="educationfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def get_education_by_id(education_id):
    try:
        education = Education.query.filter(Education.id == education_id).one()
    except NoResultFound:
        msg = f"There is no education with id {education_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {education_id}`"
        raise InvalidURL(message=msg)

    return education


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


def create_medias(media_data, user_id, education_id):
    medias = []
    if int(user_id) == g.current_user.id:
        for file in media_data:
            media_filename = files_education.save(file)
            media_url = files_education.url(media_filename)
            media = MediaEducation(media_filename=media_filename, media_url=media_url)
            education = get_education_by_id(education_id)
            media.education = education
            media.save()
            medias.append(media)
            user_edited(user_id)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_media_by_id(user_id, media_education_id):
    if int(user_id) == g.current_user.id:
        try:
            media = MediaEducation.query.filter(
                MediaEducation.id == media_education_id
            ).one()
        except NoResultFound:
            msg = f"There is no media with id {media_education_id}"
            raise RecordNotFound(message=msg)
        except InvalidURL:
            msg = f"This is not a valid URL: {media_education_id}`"
            raise InvalidURL(message=msg)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return media


def get_all_medias(user_id, education_id):
    if int(user_id) == g.current_user.id:
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
                media_filename = files_education.save(file)
                media_url = files_education.url(media_filename)
                media = MediaEducation(
                    media_filename=media_filename, media_url=media_url
                )
                education = get_education_by_id(education_id)
                media.education = education
                media.save()
                medias.append(media)
                user_edited(user_id)
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
        media = get_media_by_id(user_id, media_education_id)
        file_name = files_education.path(media.media_filename)
        if is_file(media.media_filename):
            os.remove(get_file_path(file_name))
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersMedia(message=msg)
