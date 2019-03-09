from flask import send_from_directory  # , send_file
from config import Config
from ..helper_functions.get_by_id import (
    get_officialcommunication_media_by_id,
    get_officialcomment_media_by_id,
)


def download_officialcommunication(media_officialcommunication_id):
    media = get_officialcommunication_media_by_id(media_officialcommunication_id)
    directory = Config.UPLOADED_OFFICIALCOMMUNICATIONFILES_DEST
    filename = media.filename
    response = send_from_directory(directory, filename, as_attachment=True)

    return response


def download_officialcomment(media_officialcomment_id):
    media = get_officialcomment_media_by_id(media_officialcomment_id)
    directory = Config.UPLOADED_OFFICIALCOMMUNICATIONFILES_DEST
    filename = media.filename
    response = send_from_directory(directory, filename, as_attachment=True)

    return response
