# from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
# from sqlalchemy.orm import relationship, backref
# from ..common.database import BaseModel
# from ..common.serializers import ModelSerializerMixin

# from datetime import datetime


# class Document(BaseModel, ModelSerializerMixin):
#     """
#     Education.documents.all()
#     Document.education
#     Experience.documents.all()
#     Document.experience
#     Qualification.documents.all()
#     Document.qualifications
#     """
#     __tablename__ = 'documents'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     name = Column(String)
#     url = Column(String)

#     education_id = Column(Integer, ForeignKey('educations.id'))
#     experience_id = Column(Integer, ForeignKey('experiences.id'))
#     qualification_id = Column(Integer, ForeignKey('qualifications.id'))


# class Image(BaseModel, ModelSerializerMixin):
#     """
#     Event.images.all()
#     Image.event
#     Post.images.all()
#     Image.post
#     """
#     __tablename__ = 'images'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     image_path = Column(String)

#     event_id = Column(Integer, ForeignKey('events.id'))
#     post_id = Column(Integer, ForeignKey('posts.id'))
#     message_id = Column(Integer, ForeignKey('messages.id'))
    
# class Video(BaseModel, ModelSerializerMixin):
#     """
#     Event.videos.all()
#     Video.event
#     Post.videos.all()
#     Video.post
#     """
#     __tablename__ = 'videos'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     video_path = Column(String)

#     event_id = Column(Integer, ForeignKey('events.id'))
#     post_id = Column(Integer, ForeignKey('posts.id'))
#     message_id = Column(Integer, ForeignKey('messages.id'))

# from ..bp_user.models import Education
# from ..bp_user.models import Experience
# from ..bp_user.models import Qualification
# from ..bp_event.models import Event
# from ..bp_post.models import Post
# from ..bp_message.models import Message

