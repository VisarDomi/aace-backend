from flask import g
from ..common.models import Post
from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL


def create_post(post_data):
    post = Post.new_from_dict(post_data)
    post.user = g.current_user
    post.save()
    return post


def get_post_by_id(post_id):
    try:
        result = Post.query.filter(Post.id == post_id).one()
    except NoResultFound:
        msg = f'There is no post with id {post_id}'
        raise RecordNotFound(message=msg)
    except InvalidURL:
        msg = f"This is not a valid URL: {post_id}`"
        raise InvalidURL(message=msg)
    return result


def get_all_posts():
    posts = Post.query.all()
    return posts


def update_post(post_data, post_id):
    post = get_post_by_id(post_id)
    post.update_from_dict(post_data)
    post.save()
    return post


def delete_post(post_id):
    post = get_post_by_id(post_id)
    post.delete()
