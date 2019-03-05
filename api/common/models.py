from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    Text,
    ForeignKey,
    Date,
    Table,
    Column,
)
from sqlalchemy.orm import relationship
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import base64
import os


user_group = Table(
    "user_group",
    BaseModel.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("group_id", Integer, ForeignKey("groups.id")),
)

user_notification = Table(
    "user_notification",
    BaseModel.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("notification_id", Integer, ForeignKey("notifications.id")),
)

user_event = Table(
    "user_event",
    BaseModel.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("event_id", Integer, ForeignKey("events.id")),
    Column("type_of_engagement", String),
)

user_messagegroup = Table(
    "user_messagegroup",
    BaseModel.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("messagegroup_id", Integer, ForeignKey("messagegroups.id")),
)


class Test(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)
    description = Column(String)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class User(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    # database only
    password_hash = Column(String)
    token = Column(String, unique=True)
    token_expiration = Column(DateTime)
    is_active = Column(Boolean)
    register_date = Column(DateTime, default=datetime.utcnow)

    # database only - should be many to many
    register_status = Column(String, default="blank")
    role = Column(String, default="normal_user")
    privilege = Column(String, default="normal_privilege")

    # intro
    first_name = Column(String)
    last_name = Column(String, default="no_name")
    sex = Column(String)
    summary = Column(Text)

    # intro - should be many to one
    country = Column(String)

    # contact info
    phone = Column(String)
    address = Column(String)
    birthday = Column(Date)

    # contact info - should be one to many
    website = Column(String)
    email = Column(String, unique=True)

    # comment nga administratori
    comment_from_administrator = Column(Text)

    # intro - one to many
    medias = relationship("MediaUser", back_populates="user", lazy="dynamic")

    # experiences
    experiences = relationship("Experience", back_populates="user", lazy="dynamic")

    # educations
    educations = relationship("Education", back_populates="user", lazy="dynamic")

    # skills
    skills = relationship("Skill", back_populates="user", lazy="dynamic")

    # database related one to many
    posts = relationship("Post", back_populates="user", lazy="dynamic")
    comments = relationship("Comment", back_populates="user", lazy="dynamic")
    messages = relationship("Message", back_populates="sender", lazy="dynamic")
    messagerecipients = relationship(
        "MessageRecipient", back_populates="recipient", lazy="dynamic"
    )

    # groups
    groups = relationship(
        "Group", secondary="user_group", back_populates="users", lazy="dynamic"
    )

    # events
    events = relationship(
        "Event", secondary="user_event", back_populates="users", lazy="dynamic"
    )

    # notifications
    notifications = relationship(
        "Notification",
        secondary="user_notification",
        back_populates="users",
        lazy="dynamic",
    )

    # helper relationship
    messagegroups = relationship(
        "MessageGroup",
        secondary="user_messagegroup",
        back_populates="users",
        lazy="dynamic",
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
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
        return f"{self.__class__.__name__}({self.last_name}, id = {self.id})"


class Experience(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    employer = Column(String, default="no_employer")
    company = Column(String)
    location = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    is_currently_work_here = Column(Boolean)
    description = Column(Text)

    user = relationship("User", back_populates="experiences")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship(
        "MediaExperience", back_populates="experience", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.employer}, id = {self.id})"


class Education(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    education_type = Column(String)
    degree = Column(String)
    field_of_study = Column(String, default="no_field_of_study")
    school = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    description = Column(Text)

    user = relationship("User", back_populates="educations")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("MediaEducation", back_populates="education", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.field_of_study}, id = {self.id})"


class Skill(BaseModel, ModelSerializerMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)

    releaser = Column(String)
    name = Column(String, default="no_name")
    from_date = Column(Date)
    to_date = Column(Date)
    description = Column(Text)

    user = relationship("User", back_populates="skills")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("MediaSkill", back_populates="skill", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class MediaUser(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)

    user = relationship("User", back_populates="medias")
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaExperience(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)

    experience = relationship("Experience", back_populates="medias")
    experience_id = Column(Integer, ForeignKey("experiences.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaEducation(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)

    education = relationship("Education", back_populates="medias")
    education_id = Column(Integer, ForeignKey("educations.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaSkill(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)

    skill = relationship("Skill", back_populates="medias")
    skill_id = Column(Integer, ForeignKey("skills.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class Group(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    description = Column(Text)

    # medias = relationship("Media", back_populates="skill", lazy="dynamic")

    users = relationship(
        "User", secondary="user_group", back_populates="groups", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Event(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    body = Column(Text)
    time_start = Column(DateTime, default=datetime.utcnow)
    time_end = Column(DateTime, default=datetime.utcnow)
    location = Column(Text)

    posts = relationship("Post", back_populates="event", lazy="dynamic")
    # medias = relationship("Media", back_populates="event", lazy="dynamic")

    users = relationship(
        "User", secondary="user_event", back_populates="events", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class Post(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    time = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="posts")
    user_id = Column(Integer, ForeignKey("users.id"))

    event = relationship("Event", back_populates="posts")
    event_id = Column(Integer, ForeignKey("events.id"))

    comments = relationship("Comment", back_populates="post", lazy="dynamic")
    # medias = relationship("Media", back_populates="post", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}(id = {self.id})"


class Comment(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    time = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="comments")
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="comments")
    post_id = Column(Integer, ForeignKey("posts.id"))

    # medias = relationship("Media", back_populates="comment", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}(id = {self.id})"


class Message(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    time = Column(DateTime, default=datetime.utcnow)

    sender = relationship("User", back_populates="messages")
    sender_id = Column(Integer, ForeignKey("users.id"))

    # medias = relationship("Media", back_populates="message", lazy="dynamic")

    messagerecipients = relationship(
        "MessageRecipient", back_populates="message", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}(id = {self.id})"


class MessageRecipient(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_read = Column(Boolean)

    message = relationship("Message", back_populates="messagerecipients")
    message_id = Column(Integer, ForeignKey("messages.id"))

    recipient = relationship("User", back_populates="messagerecipients")
    recipient_id = Column(Integer, ForeignKey("users.id"))

    messagegroup = relationship("MessageGroup", back_populates="messagerecipients")
    messagegroup_id = Column(Integer, ForeignKey("messagegroups.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}(id = {self.id})"


class MessageGroup(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String)

    messagerecipients = relationship(
        "MessageRecipient", back_populates="messagegroup", lazy="dynamic"
    )

    users = relationship(
        "User",
        secondary="user_messagegroup",
        back_populates="messagegroups",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Notification(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String)

    users = relationship(
        "User",
        secondary="user_notification",
        back_populates="notifications",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"
