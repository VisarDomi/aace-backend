from flask import send_from_directory  # , send_file
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordNotFound
from ..common.exceptions import InvalidURL

from ..common.models import MediaEducation, MediaExperience, MediaSkill
from config import Config
from ..bp_admin.backend import are_you_admin


def get_education_media_by_id(media_education_id):
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

    return media


@are_you_admin
def download_education(media_education_id):
    media = get_education_media_by_id(media_education_id)
    directory = Config.UPLOADED_EDUCATIONFILES_DEST
    filename = media.media_filename
    download_file = send_from_directory(directory, filename, as_attachment=True)
    return download_file


def get_experience_media_by_id(media_experience_id):
    try:
        media = MediaExperience.query.filter(
            MediaExperience.id == media_experience_id
        ).one()
    except NoResultFound:
        msg = f"There is no media with id {media_experience_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_experience_id}`"
        raise InvalidURL(message=msg)

    return media


@are_you_admin
def download_experience(media_experience_id):
    media = get_experience_media_by_id(media_experience_id)
    directory = Config.UPLOADED_EXPERIENCEFILES_DEST
    filename = media.media_filename
    download_file = send_from_directory(directory, filename, as_attachment=True)
    return download_file


def get_skill_media_by_id(media_skill_id):
    try:
        media = MediaSkill.query.filter(MediaSkill.id == media_skill_id).one()
    except NoResultFound:
        msg = f"There is no media with id {media_skill_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_skill_id}`"
        raise InvalidURL(message=msg)

    return media


@are_you_admin
def download_skill(media_skill_id):
    media = get_skill_media_by_id(media_skill_id)
    directory = Config.UPLOADED_SKILLFILES_DEST
    filename = media.media_filename
    download_file = send_from_directory(directory, filename, as_attachment=True)
    return download_file
