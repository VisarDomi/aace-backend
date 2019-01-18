from flask import g
from ..common.models import Media
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL


def create_media(media_data):
    media = Media.new_from_dict(media_data)
    media.user = g.current_user
    media.save()
    return media


def get_media_by_id(media_id):
    try:
        result = Media.query.filter(Media.id == media_id).one()
    except NoResultFound:
        msg = f'There is no media with id {media_id}'
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_medias():
    medias = Media.query.all()
    return medias


def update_media(media_data, media_id):
    media = get_media_by_id(media_id)
    media.update_from_dict(media_data)
    media.save()
    return media


def delete_media(media_id):
    media = get_media_by_id(media_id)
    media.delete()
