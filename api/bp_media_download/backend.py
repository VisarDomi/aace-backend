from flask import send_from_directory  # , send_file
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordNotFound, InvalidURL

from ..common.models import MediaOfficialCommunication
from config import Config


def get_officialcommunication_media_by_id(media_officialcommunication_id):
    try:
        media = MediaOfficialCommunication.query.filter(
            MediaOfficialCommunication.id == media_officialcommunication_id
        ).one()
    except NoResultFound:
        msg = f"There is no media with id {media_officialcommunication_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_officialcommunication_id}`"
        raise InvalidURL(message=msg)

    return media


def download_officialcommunication(media_officialcommunication_id):
    media = get_officialcommunication_media_by_id(media_officialcommunication_id)
    directory = Config.UPLOADED_OFFICIALCOMMUNICATIONFILES_DEST
    filename = media.filename
    download_file = send_from_directory(directory, filename, as_attachment=True)
    return download_file
