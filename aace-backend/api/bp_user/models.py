# from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
# from sqlalchemy.orm import relationship, backref
# from ..common.database import BaseModel
# from ..common.serializers import ModelSerializerMixin
# from datetime import datetime



# user_privilege = Table('user_privilege', BaseModel.metadata,
#             Column('user_id', Integer, ForeignKey('users.id')),
#             Column('privilege_id', Integer, ForeignKey('privileges.id')),
#             )

# user_group = Table('user_group', BaseModel.metadata,
#                     Column('user_id', Integer, ForeignKey('users.id')),
#                     Column('group_id', Integer, ForeignKey('groups.id')),
#                     )

# user_event = Table('user_event', BaseModel.metadata,
#                     Column('user_id', Integer, ForeignKey('users.id')),
#                     Column('event_id', Integer, ForeignKey('events.id')),
#                     Column('type_of_engagement', String),
#                     )

# user_messagegroup = Table('user_messagegroup',  BaseModel.metadata,
#                     Column('user_id', Integer, ForeignKey('users.id')),
#                     Column('messagegroup_id', Integer, ForeignKey('messagegroups.id')),
#                     )

# class Role(BaseModel, ModelSerializerMixin):
#     """
#     Role.users
#     User.role
#     """
#     __tablename__ = 'roles'
#     id = Column(Integer, primary_key = True, autoincrement=True)
#     name = Column(String)

#     users = relationship('User', backref='role', lazy='dynamic')

#     def __repr__(self):
#         return f"Role: {self.name}"

# class User(BaseModel, ModelSerializerMixin):
#     """
#     Role.user
#     User.role

#     User.educations.all()
#     Education.user
#     User.experiences.all()
#     Experience.user
#     User.qualifications.all()
#     Qualification.user
#     User.posts.all()
#     Post.user
#     User.comments.all()
#     Comment.user

#     User.messages.all()
#     Message.sender
#     User.messagerecipients.all()
#     MessageRecipient.recipient

#     User.privileges.all()
#     Privilege.users.all()
#     User.groups.all()
#     Group.users.all()
#     User.events.all()
#     Event.users.all()
#     User.messagegroups.all()
#     MessageGroup.users.all()
#     """
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     name = Column(String)
#     surname = Column(String)
#     email = Column(String)
#     password = Column(String)
#     phone = Column(String)
#     image_file = Column(String)
#     is_active = Column(Boolean)
    
#     role_id = Column(Integer, ForeignKey('roles.id'))

#     educations = relationship('Education', backref='user', lazy='dynamic')
#     experiences = relationship('Experience', backref='user', lazy='dynamic')
#     qualifications = relationship('Qualification', backref='user', lazy='dynamic')
#     posts = relationship('Post', backref='user', lazy='dynamic')
#     comments = relationship('Comment', backref='user', lazy='dynamic')

#     messages = relationship('Message', backref='sender', lazy='dynamic')
#     messagerecipients = relationship('MessageRecipient', backref='recipient', lazy='dynamic')

#     privileges = relationship('Privilege',
#                         secondary=user_privilege,
#                         backref=backref('users', lazy='dynamic'),
#                         lazy='dynamic')
#     groups = relationship('Group',
#                         secondary=user_group,
#                         backref=backref('users', lazy='dynamic'),
#                         lazy='dynamic')
#     events = relationship('Event',
#                         secondary=user_event,
#                         backref=backref('users', lazy='dynamic'),
#                         lazy='dynamic')
#     messagegroups = relationship('MessageGroup',
#                     secondary=user_messagegroup,
#                     backref=backref('users', lazy='dynamic'),
#                     lazy='dynamic')


#     def __repr__(self):
#         return f"User({self.name} {self.surname})"

# class Education(BaseModel, ModelSerializerMixin):
#     """
#     User.educations.all()
#     Education.user

#     Education.documents.all()
#     Document.education
#     """
#     __tablename__ = 'educations'
#     id = Column(Integer, primary_key = True, autoincrement=True)
    
#     name = Column(String)

#     user_id = Column(Integer, ForeignKey('users.id'))

#     documents = relationship('Document', backref='education', lazy='dynamic')

# class Experience(BaseModel, ModelSerializerMixin):
#     """
#     User.experiences.all()
#     Experience.user

#     Experience.documents.all()
#     Document.experience
#     """
#     __tablename__ = 'experiences'
#     id = Column(Integer, primary_key = True, autoincrement=True)
    
#     name = Column(String)

#     user_id = Column(Integer, ForeignKey('users.id'))
#     documents = relationship('Document', backref='experience', lazy='dynamic')

# class Qualification(BaseModel, ModelSerializerMixin):
#     """
#     User.qualifications.all()
#     Qualification.user

#     Qualification.documents.all()
#     Document.qualifications
#     """
#     __tablename__ = 'qualifications'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     name = Column(String)

#     user_id = Column(Integer, ForeignKey('users.id'))
#     documents = relationship('Document', backref='qualification', lazy='dynamic')

# class Privilege(BaseModel, ModelSerializerMixin):
#     """
#     User.privileges.all()
#     Privilege.users.all()
#     """
#     __tablename__ = 'privileges'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     name = Column(String)

# from ..bp_group.models import Group
# from ..bp_event.models import Event
# from ..bp_post.models import Post
# from ..bp_post.models import Comment
# from ..bp_message.models import Message
# from ..bp_message.models import MessageGroup
# from ..bp_message.models import MessageRecipient
    