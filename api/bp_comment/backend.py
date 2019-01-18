from flask import g
from ..common.models import Comment
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL


def create_comment(comment_data):
    comment = Comment.new_from_dict(comment_data)
    comment.user = g.current_user
    comment.save()
    return comment


def get_comment_by_id(comment_id):
    try:
        result = Comment.query.filter(Comment.id == comment_id).one()
    except NoResultFound:
        msg = f'There is no comment with id {comment_id}'
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {comment_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_comments():
    comments = Comment.query.all()
    return comments


def update_comment(comment_data, comment_id):
    comment = get_comment_by_id(comment_id)
    comment.update_from_dict(comment_data)
    comment.save()
    return comment


def delete_comment(comment_id):
    comment = get_comment_by_id(comment_id)
    comment.delete()
