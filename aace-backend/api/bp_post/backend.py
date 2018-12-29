from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound

from ..common.models import User, Post

from flask_login import login_manager

def create_post(post_data):
    post = Post(**post_data)
    return post


def get_post_by_id(post_id):
    try:
        result = Post.query.filter(Post.id == post_id).one()
    except NoResultFound:
        msg = 'There is no Post with `id: %s`' % id
        raise RecordNotFound(message=msg)

    return result


def get_all_postes():
    return Post.query.all()


def update_post(post_data, post_id):
    post = get_post_by_id(post_id)
    post.update(**post_data)

    return post


def delete_post(post_id):
    post = get_post_by_id(post_id)
    post.delete()
