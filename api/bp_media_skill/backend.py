from flask import g
from flask_uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from ..common.models import MediaSkill, Skill
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    CannotDeleteOthersMedia,
    InvalidURL,
    CannotGetOthersMedia,
)
import os


files_skill = UploadSet(
    name="skillfiles", extensions=AllExcept(SCRIPTS + EXECUTABLES)
)


def get_skill_by_id(skill_id):
    try:
        skill = Skill.query.filter(Skill.id == skill_id).one()
    except NoResultFound:
        msg = f"There is no skill with id {skill_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {skill_id}`"
        raise InvalidURL(message=msg)

    return skill


def create_medias(media_data, user_id, skill_id):
    medias = []
    if int(user_id) == g.current_user.id:
        if get_skill_by_id(skill_id):
            for file in media_data:
                filename = files_skill.save(file)
                url = files_skill.url(filename)
                media = MediaSkill(filename=filename, url=url)
                skill = get_skill_by_id(skill_id)
                media.skill = skill
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_media_by_id(user_id, media_skill_id):
    if int(user_id) == g.current_user.id:
        try:
            media = MediaSkill.query.filter(
                MediaSkill.id == media_skill_id
            ).one()
        except NoResultFound:
            msg = f"There is no media with id {media_skill_id}"
            raise RecordNotFound(message=msg)
        except InvalidURL:
            msg = f"This is not a valid URL: {media_skill_id}`"
            raise InvalidURL(message=msg)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return media


def get_all_medias(user_id, skill_id):
    if int(user_id) == g.current_user.id:
        medias = MediaSkill.query.filter(
            MediaSkill.skill_id == int(skill_id)
        ).all()
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def update_media(media_data, user_id, skill_id, media_skill_id):
    if int(user_id) == g.current_user.id:
        medias = []
        media = MediaSkill.query.filter(
            MediaSkill.id == media_skill_id
        ).one_or_none()
        for file in media_data:
            if file and media:
                delete_media(user_id, media_skill_id)
                filename = files_skill.save(file)
                url = files_skill.url(filename)
                media = MediaSkill(
                    filename=filename, url=url
                )
                skill = get_skill_by_id(skill_id)
                media.skill = skill
                media.save()
                medias.append(media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return medias


def get_file_path(file_name):
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
    FILE_TO_PATH = "static/files/skill"
    file_path = os.path.join(parent_dir, FILE_TO_PATH)
    f_path = os.path.join(file_path, file_name)

    return f_path


def is_file(file_name):
    this_file_path = get_file_path(file_name)

    return os.path.exists(this_file_path)


def delete_media(user_id, media_skill_id):
    if int(user_id) == g.current_user.id:
        media = get_media_by_id(user_id, media_skill_id)
        file_name = files_skill.path(media.filename)
        if is_file(media.filename):
            os.remove(get_file_path(file_name))
        media.delete()
    else:
        msg = "You can't delete other people's profile."
        raise CannotDeleteOthersMedia(message=msg)
