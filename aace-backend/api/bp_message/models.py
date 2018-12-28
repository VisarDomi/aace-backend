# from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
# from sqlalchemy.orm import relationship, backref
# from ..common.database import BaseModel
# from ..common.serializers import ModelSerializerMixin

# from datetime import datetime


# class Message(BaseModel, ModelSerializerMixin):
#     """
#     User.messages.all()
#     Message.sender

#     Message.messagerecipients.all()
#     MessageRecipient.message
#     Message.images.all()
#     Image.message
#     Message.videos.all()
#     Video.message
#     """
#     __tablename__ = 'messages'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     text = Column(Text)
#     timestamp = Column(DateTime, default=datetime.utcnow)

#     sender_id = Column(Integer, ForeignKey('users.id'))

#     messagerecipients = relationship('MessageRecipient', backref='message', lazy='dynamic')
#     images = relationship('Image', backref='message', lazy='dynamic')
#     videos = relationship('Video', backref='message', lazy='dynamic')

# class MessageRecipient(BaseModel, ModelSerializerMixin):
#     """
#     Message.messagerecipients.all()
#     MessageRecipient.message
#     User.messagerecipients.all()
#     MessageRecipient.recipient
#     MessageGroup.messagerecipients.all()
#     MessageRecipient.messagegroup
#     """
#     __tablename__ = 'messagerecipients'
#     id = Column(Integer, primary_key = True, autoincrement=True)
#     is_read = Column(Boolean)

#     message_id = Column(Integer, ForeignKey('messages.id'))
#     recipient_id = Column(Integer, ForeignKey('users.id'))
#     recipientgroup_id = Column(Integer, ForeignKey('messagegroups.id'))


# class MessageGroup(BaseModel, ModelSerializerMixin):
#     """
#     MessageGroup.messagerecipients.all()
#     MessageRecipient.messagegroup

#     User.messagegroups.all()
#     MessageGroup.users.all()
#     """
#     __tablename__ = 'messagegroups'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     name = Column(String)

#     messagerecipients = relationship('MessageRecipient', backref='messagegroup', lazy='dynamic')

# from ..bp_multimedia.models import Image
# from ..bp_multimedia.models import Video
# from ..bp_user.models import Experience

# from ..bp_user.models import User