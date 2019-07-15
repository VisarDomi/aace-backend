from flask import g
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL, CannotGetOthersMedia


def get_entity(entity_id, Entity):
    try:
        entity = Entity.query.filter(Entity.id == int(entity_id)).one()
    except NoResultFound:
        msg = f"There is no entity with id {entity_id}"
        raise RecordNotFound(message=msg)
    except (InvalidURL, ValueError):
        msg = f"This is not a valid URL: {entity_id}`"
        raise InvalidURL(message=msg)

    return entity


def same_user_get_media(user_id, media_id, Media):
    if int(user_id) == g.current_user.id or g.current_user.role == "admin":
        media = get_entity(media_id, Media)
    else:
        msg = f"You can't get other people's media."
        raise CannotGetOthersMedia(message=msg)

    return media
