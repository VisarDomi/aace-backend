from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaEvent
import os
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_event_by_id
from ..helper_functions.get_media_by_id import get_event_media_by_id


files_event = UploadSet(name="eventfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES))


@admin_required
def create_medias(media_data, event_id):
    medias = []
    if get_event_by_id(event_id):
        for file in media_data:
            filename = files_event.save(file)
            url = files_event.url(filename)
            media = MediaEvent(filename=filename, url=url)
            media.event = get_event_by_id(event_id)
            media.save()
            medias.append(media)

    return medias


def get_medias(event_id):
    medias = MediaEvent.query.filter(MediaEvent.event_id == int(event_id)).all()

    return medias


@admin_required
def update_media(media_data, event_id, media_event_id):
    medias = []
    media = MediaEvent.query.filter(MediaEvent.id == media_event_id).one_or_none()
    for file in media_data:
        if file and media:
            delete_media(event_id, media_event_id)
            filename = files_event.save(file)
            url = files_event.url(filename)
            media = MediaEvent(filename=filename, url=url)
            media.event = get_event_by_id(event_id)
            media.save()
            medias.append(media)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/event"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


@admin_required
def delete_media(media_event_id):
    media = get_event_media_by_id(media_event_id)
    file_name = files_event.path(media.filename)
    if is_file(media.filename):
        os.remove(get_file_path(file_name))
    media.delete()
