from flask import g
from ..common.models import Comment
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotChangeOthersProfile,
    CannotCommentOnOthersProfile,
)


def create_comment(comment_data, user_id):
    if int(user_id) == g.current_user.id:
        comment = Comment.new_from_dict(comment_data)
        comment.user = g.current_user
        comment.save()
    else:
        msg = f"You can't comment on other people's profile."
        raise CannotCommentOnOthersProfile(message=msg)
    return comment


def get_comment_by_id(comment_id):
    try:
        result = Comment.query.filter(Comment.id == comment_id).one()
    except NoResultFound:
        msg = f"There is no comment with id {comment_id}"
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {comment_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_comments(user_id):
    comments = Comment.query.filter(Comment.user_id == int(user_id)).all()
    return comments


def update_comment(comment_data, user_id, comment_id):
    if int(user_id) == g.current_user.id:
        comment = get_comment_by_id(comment_id)
        comment.update_from_dict(comment_data)
        comment.save()
    else:
        msg = f"You can't change other people's profile."
        raise CannotChangeOthersProfile(message=msg)
    return comment


def delete_comment(comment_id):
    comment = get_comment_by_id(comment_id)
    comment.delete()
