from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import base64
import os

user_privilege = Table('user_privilege', BaseModel.metadata,
            Column('user_id', Integer, ForeignKey('users.id')),
            Column('privilege_id', Integer, ForeignKey('privileges.id')),
            )

user_group = Table('user_group', BaseModel.metadata,
                    Column('user_id', Integer, ForeignKey('users.id')),
                    Column('group_id', Integer, ForeignKey('groups.id')),
                    )

user_event = Table('user_event', BaseModel.metadata,
                    Column('user_id', Integer, ForeignKey('users.id')),
                    Column('event_id', Integer, ForeignKey('events.id')),
                    Column('type_of_engagement', String(200)),
                    )

user_messagegroup = Table('user_messagegroup',  BaseModel.metadata,
                    Column('user_id', Integer, ForeignKey('users.id')),
                    Column('messagegroup_id', Integer, ForeignKey('messagegroups.id')),
                    )

class Role(BaseModel, ModelSerializerMixin):
    """
    Role.users
    User.role
    """
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))

    users = relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f"Role: {self.name}"

class User(BaseModel, ModelSerializerMixin):
    """
    Role.users.all()
    User.role

    User.educations.all()
    Education.user
    User.experiences.all()
    Experience.user
    User.qualifications.all()
    Qualification.user
    User.posts.all()
    Post.user
    User.comments.all()
    Comment.user

    User.messages.all()
    Message.sender
    User.messagerecipients.all()
    MessageRecipient.recipient

    User.privileges.all()
    Privilege.users.all()
    User.groups.all()
    Group.users.all()
    User.events.all()
    Event.users.all()
    User.messagegroups.all()
    MessageGroup.users.all()
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(200))
    surname = Column(String(200))
    email = Column(String(200), unique=True)
    password_hash = Column(String(200))
    token = Column(String(200), index=True, unique=True)
    token_expiration = Column(DateTime)
    phone = Column(String(200))
    image_file = Column(String(200))
    is_active = Column(Boolean)
    
    role_id = Column(Integer, ForeignKey('roles.id'))

    educations = relationship('Education', backref='user', lazy='dynamic')
    experiences = relationship('Experience', backref='user', lazy='dynamic')
    qualifications = relationship('Qualification', backref='user', lazy='dynamic')
    posts = relationship('Post', backref='user', lazy='dynamic')
    comments = relationship('Comment', backref='user', lazy='dynamic')

    messages = relationship('Message', backref='sender', lazy='dynamic')
    messagerecipients = relationship('MessageRecipient', backref='recipient', lazy='dynamic')

    privileges = relationship('Privilege',
                        secondary=user_privilege,
                        backref=backref('users', lazy='dynamic'),
                        lazy='dynamic')
    groups = relationship('Group',
                        secondary=user_group,
                        backref=backref('users', lazy='dynamic'),
                        lazy='dynamic')
    events = relationship('Event',
                        secondary=user_event,
                        backref=backref('users', lazy='dynamic'),
                        lazy='dynamic')
    messagegroups = relationship('MessageGroup',
                    secondary=user_messagegroup,
                    backref=backref('users', lazy='dynamic'),
                    lazy='dynamic')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        self.save()
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def __repr__(self):
        return f"User({self.name} {self.surname})"

class Education(BaseModel, ModelSerializerMixin):
    """
    User.educations.all()
    Education.user

    Education.documents.all()
    Document.education
    """
    __tablename__ = 'educations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(String(200))

    user_id = Column(Integer, ForeignKey('users.id'))

    documents = relationship('Document', backref='education', lazy='dynamic')

class Experience(BaseModel, ModelSerializerMixin):
    """
    User.experiences.all()
    Experience.user

    Experience.documents.all()
    Document.experience
    """
    __tablename__ = 'experiences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(String(200))

    user_id = Column(Integer, ForeignKey('users.id'))
    documents = relationship('Document', backref='experience', lazy='dynamic')

class Qualification(BaseModel, ModelSerializerMixin):
    """
    User.qualifications.all()
    Qualification.user

    Qualification.documents.all()
    Document.qualifications
    """
    __tablename__ = 'qualifications'
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(200))

    user_id = Column(Integer, ForeignKey('users.id'))
    documents = relationship('Document', backref='qualification', lazy='dynamic')

class Document(BaseModel, ModelSerializerMixin):
    """
    Education.documents.all()
    Document.education
    Experience.documents.all()
    Document.experience
    Qualification.documents.all()
    Document.qualifications
    """
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(200))
    url = Column(String(200))

    education_id = Column(Integer, ForeignKey('educations.id'))
    experience_id = Column(Integer, ForeignKey('experiences.id'))
    qualification_id = Column(Integer, ForeignKey('qualifications.id'))

class Privilege(BaseModel, ModelSerializerMixin):
    """
    User.privileges.all()
    Privilege.users.all()
    """
    __tablename__ = 'privileges'
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(200))
    
class Group(BaseModel, ModelSerializerMixin):
    """
    User.groups.all()
    Group.users.all()
    """
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(200), unique=True)

    def __repr__(self):
        return 'Group: {}'.format(self.name)

class Event(BaseModel, ModelSerializerMixin):
    """
    Event.posts.all()
    Post.event
    Event.images.all()
    Image.event
    Event.videos.all()
    Video.event

    User.events.all()
    Event.users.all()
    """
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    posts = relationship('Post', backref='event', lazy='dynamic')
    images = relationship('Image', backref='event', lazy='dynamic')
    videos = relationship('Video', backref='event', lazy='dynamic')

class Post(BaseModel, ModelSerializerMixin):
    """
    User.posts.all()
    Post.user
    Event.posts.all()
    Post.event

    Post.comments.all()
    Comment.post
    Post.images.all()
    Image.post
    Post.videos.all()
    Video.post
    """
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)

    text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

    comments = relationship('Comment', backref='post', lazy='dynamic')
    images = relationship('Image', backref='post', lazy='dynamic')
    videos = relationship('Video', backref='post', lazy='dynamic')

class Comment(BaseModel, ModelSerializerMixin):
    """
    User.comments.all()
    Comment.user
    Post.comments.all()
    Comment.post
    """
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

class Message(BaseModel, ModelSerializerMixin):
    """
    User.messages.all()
    Message.sender

    Message.messagerecipients.all()
    MessageRecipient.message
    Message.images.all()
    Image.message
    Message.videos.all()
    Video.message
    """
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)

    text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sender_id = Column(Integer, ForeignKey('users.id'))

    messagerecipients = relationship('MessageRecipient', backref='message', lazy='dynamic')
    images = relationship('Image', backref='message', lazy='dynamic')
    videos = relationship('Video', backref='message', lazy='dynamic')

class MessageRecipient(BaseModel, ModelSerializerMixin):
    """
    Message.messagerecipients.all()
    MessageRecipient.message
    User.messagerecipients.all()
    MessageRecipient.recipient
    MessageGroup.messagerecipients.all()
    MessageRecipient.messagegroup
    """
    __tablename__ = 'messagerecipients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    is_read = Column(Boolean)

    message_id = Column(Integer, ForeignKey('messages.id'))
    recipient_id = Column(Integer, ForeignKey('users.id'))
    recipientgroup_id = Column(Integer, ForeignKey('messagegroups.id'))


class MessageGroup(BaseModel, ModelSerializerMixin):
    """
    MessageGroup.messagerecipients.all()
    MessageRecipient.messagegroup

    User.messagegroups.all()
    MessageGroup.users.all()
    """
    __tablename__ = 'messagegroups'
    id = Column(Integer, primary_key = True, autoincrement=True)

    name = Column(String(200))

    messagerecipients = relationship('MessageRecipient', backref='messagegroup', lazy='dynamic')


class Image(BaseModel, ModelSerializerMixin):
    """
    Event.images.all()
    Image.event
    Post.images.all()
    Image.post
    """
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, autoincrement=True)

    image_path = Column(String(200))

    event_id = Column(Integer, ForeignKey('events.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    message_id = Column(Integer, ForeignKey('messages.id'))
    
class Video(BaseModel, ModelSerializerMixin):
    """
    Event.videos.all()
    Video.event
    Post.videos.all()
    Video.post
    """
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True, autoincrement=True)

    video_path = Column(String(200))

    event_id = Column(Integer, ForeignKey('events.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    message_id = Column(Integer, ForeignKey('messages.id'))


