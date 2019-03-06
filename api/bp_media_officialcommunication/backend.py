from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import MediaOfficialCommunication, OfficialCommunication
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL
import os
from ..bp_admin.backend import are_you_admin


files_officialcommunication = UploadSet(
    name="officialcommunicationfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def get_officialcommunication_by_id(officialcommunication_id):
    try:
        officialcommunication = OfficialCommunication.query.filter(
            OfficialCommunication.id == officialcommunication_id
        ).one()
    except NoResultFound:
        msg = f"There is no OfficialCommunication with `id: {officialcommunication_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {officialcommunication_id}`"
        raise InvalidURL(message=msg)

    return officialcommunication


@are_you_admin
def create_medias(media_data, officialcommunication_id):
    medias = []
    for file in media_data:
        filename = files_officialcommunication.save(file)
        url = files_officialcommunication.url(filename)
        media = MediaOfficialCommunication(filename=filename, url=url)
        media.officialcommunication = get_officialcommunication_by_id(
            officialcommunication_id
        )
        media.save()
        medias.append(media)

    return medias


def get_media_by_id(officialcommunication_id, media_officialcommunication_id):
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


def get_all_medias(officialcommunication_id):
    medias = MediaOfficialCommunication.query.filter(
        MediaOfficialCommunication.officialcommunication_id
        == int(officialcommunication_id)
    ).all()

    return medias


@are_you_admin
def update_media(media_data, officialcommunication_id, media_officialcommunication_id):
    medias = []
    media = MediaOfficialCommunication.query.filter(
        MediaOfficialCommunication.id == media_officialcommunication_id
    ).one_or_none()
    for file in media_data:
        if file and media:
            delete_media(officialcommunication_id, media_officialcommunication_id)
            filename = files_officialcommunication.save(file)
            url = files_officialcommunication.url(filename)
            media = MediaOfficialCommunication(filename=filename, url=url)
            media.officialcommunication = get_officialcommunication_by_id(
                officialcommunication_id
            )
            media.save()
            medias.append(media)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/officialcommunication"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


@are_you_admin
def delete_media(officialcommunication_id, media_officialcommunication_id):
    media = get_media_by_id(officialcommunication_id, media_officialcommunication_id)
    file_name = files_officialcommunication.path(media.filename)
    if is_file(media.filename):
        os.remove(get_file_path(file_name))
    media.delete()
