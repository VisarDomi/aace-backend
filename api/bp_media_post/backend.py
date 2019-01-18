from flask import g
from ..common.models import Media
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL, CannotChangeOthersProfile


def create_media(media_data, user_id, post_id):
    if int(user_id) == g.current_user.id:
        media = Media.new_from_dict(media_data)
        media.user = g.current_user
        media.post = g.current_user.posts.filter_by(id=int(post_id)).one()
        media.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return media


def get_media_by_id(media_id):
    try:
        result = Media.query.filter(Media.id == media_id).one()
    except NoResultFound:
        msg = f"There is no media with id {media_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {media_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_medias():
    medias = Media.query.all()
    return medias


def update_media(media_data, user_id, media_id):
    if int(user_id) == g.current_user.id:
        media = get_media_by_id(media_id)
        media.update_from_dict(media_data)
        media.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return media


def delete_media(media_id):
    media = get_media_by_id(media_id)
    media.delete()
