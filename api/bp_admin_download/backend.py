from flask import send_from_directory  # , send_file
from config import Config
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import (
    get_education_media_by_id,
    get_experience_media_by_id,
    get_skill_media_by_id,
)


@admin_required
def download_education(media_education_id):
    media = get_education_media_by_id(media_education_id)
    directory = Config.UPLOADED_EDUCATIONFILES_DEST
    filename = media.filename
    response = send_from_directory(directory, filename, as_attachment=True)

    return response


@admin_required
def download_experience(media_experience_id):
    media = get_experience_media_by_id(media_experience_id)
    directory = Config.UPLOADED_EXPERIENCEFILES_DEST
    filename = media.filename
    response = send_from_directory(directory, filename, as_attachment=True)

    return response


@admin_required
def download_skill(media_skill_id):
    media = get_skill_media_by_id(media_skill_id)
    directory = Config.UPLOADED_SKILLFILES_DEST
    filename = media.filename
    response = send_from_directory(directory, filename, as_attachment=True)

    return response
