# from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
# from sqlalchemy.orm import relationship, backref
# from ..common.database import BaseModel
# from ..common.serializers import ModelSerializerMixin

# from datetime import datetime


# class Event(BaseModel, ModelSerializerMixin):
#     """
#     Event.posts.all()
#     Post.event
#     Event.images.all()
#     Image.event
#     Event.videos.all()
#     Video.event

#     User.events.all()
#     Event.users.all()
#     """
#     __tablename__ = 'events'
#     id = Column(Integer, primary_key = True, autoincrement=True)
    
#     text = Column(Text)
#     timestamp = Column(DateTime, default=datetime.utcnow)
    
#     posts = relationship('Post', backref='event', lazy='dynamic')
#     images = relationship('Image', backref='event', lazy='dynamic')
#     videos = relationship('Video', backref='event', lazy='dynamic')

# from ..bp_post.models import Post
# from ..bp_multimedia.models import Image
# from ..bp_multimedia.models import Video