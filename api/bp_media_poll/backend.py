from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaPoll
import os
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_poll_by_id
from ..helper_functions.get_media_by_id import get_poll_media_by_id


files_poll = UploadSet(name="pollfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES))


@admin_required
def create_medias(media_data, poll_id):
    medias = []
    if get_poll_by_id(poll_id):
        for file in media_data:
            filename = files_poll.save(file)
            url = files_poll.url(filename)
            media = MediaPoll(filename=filename, url=url)
            media.poll = get_poll_by_id(poll_id)
            media.save()
            medias.append(media)

    return medias


def get_medias(poll_id):
    medias = MediaPoll.query.filter(MediaPoll.poll_id == int(poll_id)).all()

    return medias


@admin_required
def update_media(media_data, poll_id, media_poll_id):
    medias = []
    media = MediaPoll.query.filter(MediaPoll.id == media_poll_id).one_or_none()
    for file in media_data:
        if file and media:
            delete_media(poll_id, media_poll_id)
            filename = files_poll.save(file)
            url = files_poll.url(filename)
            media = MediaPoll(filename=filename, url=url)
            media.poll = get_poll_by_id(poll_id)
            media.save()
            medias.append(media)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/poll"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


@admin_required
def delete_media(media_poll_id):
    media = get_poll_media_by_id(media_poll_id)
    file_name = files_poll.path(media.filename)
    if is_file(media.filename):
        os.remove(get_file_path(file_name))
    media.delete()
