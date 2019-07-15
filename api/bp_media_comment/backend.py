from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..models.medias import MediaComment
import os
from ..helper_functions.get_by_id import get_comment_by_id
from ..helper_functions.get_media_by_id import get_comment_media_by_id
from ..common.exceptions import CannotGetOthersMedia


files_comment = UploadSet(
    name="commentfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def create_medias(media_data, comment_id):
    medias = []
    comment = get_comment_by_id(comment_id)
    if comment:
        if comment.author == g.current_user:
            for file in media_data:
                filename = files_comment.save(file)
                url = files_comment.url(filename)
                media = MediaComment(filename=filename, url=url)
                media.comment = comment
                media.save()
                medias.append(media)
        else:
            msg = f"You can't get other people's media."
            raise CannotGetOthersMedia(message=msg)

    return medias


def get_medias(comment_id):
    medias = MediaComment.query.filter(MediaComment.comment_id == int(comment_id)).all()

    return medias


def update_media(media_data, comment_id, media_comment_id):
    medias = []
    media = MediaComment.query.filter(MediaComment.id == media_comment_id).one_or_none()
    comment = get_comment_by_id(comment_id)
    if comment:
        if comment.author == g.current_user:
            for file in media_data:
                if file and media:
                    delete_media(comment_id, media_comment_id)
                    filename = files_comment.save(file)
                    url = files_comment.url(filename)
                    media = MediaComment(filename=filename, url=url)
                    media.comment = comment
                    media.save()
                    medias.append(media)
        else:
            msg = f"You can't get other people's media."
            raise CannotGetOthersMedia(message=msg)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/comment"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


def delete_media(comment_id, media_comment_id):
    comment = get_comment_by_id(comment_id)
    secure = False
    # needs security
    secure = True
    if comment and secure:
        if comment.author == g.current_user:
            media = get_comment_media_by_id(media_comment_id)
            file_name = files_comment.path(media.filename)
            if is_file(media.filename):
                os.remove(get_file_path(file_name))
            media.delete()
        else:
            msg = f"You can't get other people's media."
            raise CannotGetOthersMedia(message=msg)
