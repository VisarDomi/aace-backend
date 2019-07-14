from flask import send_from_directory  # , send_file
from config import Config
from ..helper_functions.get_by_id import (
    get_communication_media_by_id,
    get_comment_media_by_id,
)


def download_communication(media_communication_id):
    media = get_communication_media_by_id(media_communication_id)
    directory = Config.UPLOADED_COMMUNICATIONFILES_DEST
    filename = media.filename
    response = send_from_directory(directory, filename, as_attachment=True)

    return response


def download_comment(media_comment_id):
    media = get_comment_media_by_id(media_comment_id)
    directory = Config.UPLOADED_COMMUNICATIONFILES_DEST
    filename = media.filename
    response = send_from_directory(directory, filename, as_attachment=True)

    return response
