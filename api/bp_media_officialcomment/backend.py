from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import MediaOfficialComment
import os
from ..helper_functions.get_by_id import (
    get_officialcomment_by_id,
    get_officialcomment_media_by_id,
)
from ..common.exceptions import CannotGetOthersMedia


files_officialcomment = UploadSet(
    name="officialcommentfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def create_medias(media_data, officialcommunication_id, officialcomment_id):
    medias = []
    officialcomment = get_officialcomment_by_id(
        officialcommunication_id, officialcomment_id
    )
    if officialcomment:
        if officialcomment.author == g.current_user:
            for file in media_data:
                filename = files_officialcomment.save(file)
                url = files_officialcomment.url(filename)
                media = MediaOfficialComment(filename=filename, url=url)
                media.officialcomment = officialcomment
                media.save()
                medias.append(media)
        else:
            msg = f"You can't get other people's media."
            raise CannotGetOthersMedia(message=msg)

    return medias


def get_all_medias(officialcommunication_id, officialcomment_id):
    medias = MediaOfficialComment.query.filter(
        MediaOfficialComment.officialcomment_id == int(officialcomment_id)
    ).all()

    return medias


def update_media(
    media_data, officialcommunication_id, officialcomment_id, media_officialcomment_id
):
    medias = []
    media = MediaOfficialComment.query.filter(
        MediaOfficialComment.id == media_officialcomment_id
    ).one_or_none()
    officialcomment = get_officialcomment_by_id(
        officialcommunication_id, officialcomment_id
    )
    if officialcomment:
        if officialcomment.author == g.current_user:
            for file in media_data:
                if file and media:
                    delete_media(
                        officialcommunication_id,
                        officialcomment_id,
                        media_officialcomment_id,
                    )
                    filename = files_officialcomment.save(file)
                    url = files_officialcomment.url(filename)
                    media = MediaOfficialComment(filename=filename, url=url)
                    media.officialcomment = officialcomment
                    media.save()
                    medias.append(media)
        else:
            msg = f"You can't get other people's media."
            raise CannotGetOthersMedia(message=msg)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/officialcomment"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


# login
def delete_media(
    officialcommunication_id, officialcomment_id, media_officialcomment_id
):
    officialcomment = get_officialcomment_by_id(
        officialcommunication_id, officialcomment_id
    )
    if officialcomment:
        if officialcomment.author == g.current_user:
            media = get_officialcomment_media_by_id(media_officialcomment_id)
            file_name = files_officialcomment.path(media.filename)
            if is_file(media.filename):
                os.remove(get_file_path(file_name))
            media.delete()
        else:
            msg = f"You can't get other people's media."
            raise CannotGetOthersMedia(message=msg)
