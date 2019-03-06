from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import MediaOfficialComment, OfficialComment
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL
import os


files_officialcomment = UploadSet(
    name="officialcommentfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def get_officialcomment_by_id(officialcomment_id):
    try:
        officialcomment = OfficialComment.query.filter(
            OfficialComment.id == officialcomment_id
        ).one()
    except NoResultFound:
        msg = f"There is no OfficialComment with `id: {officialcomment_id}`"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {officialcomment_id}`"
        raise InvalidURL(message=msg)

    return officialcomment


def create_medias(media_data, officialcomment_id):
    medias = []
    for file in media_data:
        filename = files_officialcomment.save(file)
        url = files_officialcomment.url(filename)
        media = MediaOfficialComment(filename=filename, url=url)
        media.officialcomment = get_officialcomment_by_id(officialcomment_id)
        media.save()
        medias.append(media)

    return medias


def get_media_by_id(officialcomment_id, media_officialcomment_id):
    try:
        media = MediaOfficialComment.query.filter(
            MediaOfficialComment.id == media_officialcomment_id
        ).one()
    except NoResultFound:
        msg = f"There is no media with id {media_officialcomment_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_officialcomment_id}`"
        raise InvalidURL(message=msg)

    return media


def get_all_medias(officialcomment_id):
    medias = MediaOfficialComment.query.filter(
        MediaOfficialComment.officialcomment_id == int(officialcomment_id)
    ).all()

    return medias


def update_media(media_data, officialcomment_id, media_officialcomment_id):
    medias = []
    media = MediaOfficialComment.query.filter(
        MediaOfficialComment.id == media_officialcomment_id
    ).one_or_none()
    for file in media_data:
        if file and media:
            delete_media(officialcomment_id, media_officialcomment_id)
            filename = files_officialcomment.save(file)
            url = files_officialcomment.url(filename)
            media = MediaOfficialComment(filename=filename, url=url)
            media.officialcomment = get_officialcomment_by_id(officialcomment_id)
            media.save()
            medias.append(media)

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


def delete_media(officialcomment_id, media_officialcomment_id):
    media = get_media_by_id(officialcomment_id, media_officialcomment_id)
    file_name = files_officialcomment.path(media.filename)
    if is_file(media.filename):
        os.remove(get_file_path(file_name))
    media.delete()
