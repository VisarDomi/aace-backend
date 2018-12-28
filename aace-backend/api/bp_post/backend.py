from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound

from ..common.models import User, Post

from flask_login import login_manager

def create_post(post_data):
    post = Post(**post_data)
    return post


# def get_foss_by_id(foss_id):
#     try:
#         result = Foss.query.filter(Foss.id == foss_id).one()
#     except NoResultFound:
#         msg = 'There is no Foss with `id: %s`' % id
#         raise RecordNotFound(message=msg)

#     return result


# def get_all_fosses():
#     return Foss.query.all()


# def update_foss(foss_data, foss_id):
#     foss = get_foss_by_id(foss_id)
#     foss.update(**foss_data)

#     return foss


# def delete_foss(foss_id):
#     foss = get_foss_by_id(foss_id)
#     foss.delete()
