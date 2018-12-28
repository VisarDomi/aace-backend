# from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
# from sqlalchemy.orm import relationship, backref
# from ..common.database import BaseModel
# from ..common.serializers import ModelSerializerMixin

# from datetime import datetime



# class Post(BaseModel, ModelSerializerMixin):
#     """
#     User.posts.all()
#     Post.user
#     Event.posts.all()
#     Post.event

#     Post.comments.all()
#     Comment.post
#     Post.images.all()
#     Image.post
#     Post.videos.all()
#     Video.post
#     """
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key = True, autoincrement=True)
    
#     text = Column(Text)
#     timestamp = Column(DateTime, default=datetime.utcnow)

#     user_id = Column(Integer, ForeignKey('users.id'))
#     event_id = Column(Integer, ForeignKey('events.id'))
    
#     comments = relationship('Comment', backref='post', lazy='dynamic')
#     images = relationship('Image', backref='post', lazy='dynamic')
#     videos = relationship('Video', backref='post', lazy='dynamic')
    
# class Comment(BaseModel, ModelSerializerMixin):
#     """
#     User.comments.all()
#     Comment.user
#     Post.comments.all()
#     Comment.post
#     """
#     __tablename__ = 'comments'
#     id = Column(Integer, primary_key = True, autoincrement=True)
    
#     text = Column(Text)
#     timestamp = Column(DateTime, default=datetime.utcnow)

#     user_id = Column(Integer, ForeignKey('users.id'))
#     post_id = Column(Integer, ForeignKey('posts.id'))


# from ..bp_event.models import Event
# from ..bp_multimedia.models import Image
# from ..bp_multimedia.models import Video
# from ..bp_post.models import Comment
# from ..bp_user.models import User