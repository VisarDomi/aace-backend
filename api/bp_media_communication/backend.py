from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaCommunication
import os
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import (
    get_communication_by_id,
    get_communication_media_by_id,
)


files_communication = UploadSet(
    name="communicationfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


@admin_required
def create_medias(media_data, communication_id):
    medias = []
    if get_communication_by_id(communication_id):
        for file in media_data:
            filename = files_communication.save(file)
            url = files_communication.url(filename)
            media = MediaCommunication(filename=filename, url=url)
            media.communication = get_communication_by_id(
                communication_id
            )
            media.save()
            medias.append(media)

    return medias


def get_all_medias(communication_id):
    medias = MediaCommunication.query.filter(
        MediaCommunication.communication_id
        == int(communication_id)
    ).all()

    return medias


@admin_required
def update_media(media_data, communication_id, media_communication_id):
    medias = []
    media = MediaCommunication.query.filter(
        MediaCommunication.id == media_communication_id
    ).one_or_none()
    for file in media_data:
        if file and media:
            delete_media(communication_id, media_communication_id)
            filename = files_communication.save(file)
            url = files_communication.url(filename)
            media = MediaCommunication(filename=filename, url=url)
            media.communication = get_communication_by_id(
                communication_id
            )
            media.save()
            medias.append(media)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/communication"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


@admin_required
def delete_media(media_communication_id):
    media = get_communication_media_by_id(media_communication_id)
    file_name = files_communication.path(media.filename)
    if is_file(media.filename):
        os.remove(get_file_path(file_name))
    media.delete()
