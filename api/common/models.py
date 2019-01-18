from sqlathanor import AttributeConfiguration, relationship, Column, Table
from sqlalchemy import Integer, String, Boolean, DateTime, Text, ForeignKey, Date
from ..common.database import BaseModel, CustomBase
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import base64
import os


user_group = Table(
    "user_group",
    BaseModel.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
    Column(
        "group_id",
        Integer,
        ForeignKey("groups.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
)

user_notification = Table(
    "user_notification",
    BaseModel.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
    Column(
        "notification_id",
        Integer,
        ForeignKey("notifications.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
)

user_event = Table(
    "user_event",
    BaseModel.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
    Column(
        "event_id",
        Integer,
        ForeignKey("events.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
    Column(
        "type_of_engagement",
        String,
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
)

user_messagegroup = Table(
    "user_messagegroup",
    BaseModel.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
    Column(
        "messagegroup_id",
        Integer,
        ForeignKey("messagegroups.id"),
        supports_dict=(True, True),
        supports_json=(True, True),
    ),
)


class User(BaseModel, CustomBase):
    __tablename__ = "users"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        #                                          put=false, get=true
        AttributeConfiguration(
            name="token", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="is_active", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="register_date",
            supports_dict=(False, True),
            supports_json=(False, True),
        ),
        AttributeConfiguration(
            name="register_status",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="role", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="privilege", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="profile_picture",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="background_picture",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="first_name", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="last_name", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="headline", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="summary", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="country", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="industry", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="phone", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="address", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="birthday", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="website", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="email", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="experiences", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="educations", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="accomplishments",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="posts", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="comments", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messages", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messagerecipients",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="groups", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="events", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messagegroups", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
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
    profile_picture = Column(String)
    background_picture = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    headline = Column(String)
    summary = Column(Text)

    # intro - should be many to one
    country = Column(String)
    industry = Column(String)

    # intro - one to many
    medias = relationship("Media", back_populates="user", lazy="dynamic")

    # contact info
    phone = Column(String)
    address = Column(String)
    birthday = Column(Date)

    # contact info - should be one to many
    website = Column(String)
    email = Column(String, unique=True)

    # experiences
    experiences = relationship("Experience", back_populates="user", lazy="dynamic")

    # educations
    educations = relationship("Education", back_populates="user", lazy="dynamic")

    # accomplishments
    accomplishments = relationship(
        "Accomplishment", back_populates="user", lazy="dynamic"
    )

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

    def get_token(self, expires_in=36_000_000):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=3_600_000):
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
        return f"User({self.id} {self.email})"


class Experience(BaseModel, CustomBase):
    __tablename__ = "experiences"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="title", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="company", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="location", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="from_date", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="to_date", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="is_currently_work_here", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="description", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String)
    company = Column(String)
    location = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    is_currently_work_here = Column(Boolean)
    description = Column(Text)

    user = relationship("User", back_populates="experiences")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("Media", back_populates="experience", lazy="dynamic")

    def __repr__(self):
        return f"Experience({self.id} {self.title})"


class Education(BaseModel, CustomBase):
    __tablename__ = "educations"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="school", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="degree", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="field_of_study",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="from_year", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="to_year", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="grade", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="description", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    school = Column(String)
    degree = Column(String)
    field_of_study = Column(String)
    from_year = Column(Date)
    to_year = Column(Date)
    grade = Column(String)
    description = Column(Text)

    user = relationship("User", back_populates="educations")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("Media", back_populates="education", lazy="dynamic")

    def __repr__(self):
        return f"Education({self.id} {self.school})"


class Accomplishment(BaseModel, CustomBase):
    __tablename__ = "accomplishments"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="name", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="description", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String)
    description = Column(Text)

    user = relationship("User", back_populates="accomplishments")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("Media", back_populates="accomplishment", lazy="dynamic")

    def __repr__(self):
        return f"Accomplishment({self.id} {self.name})"


class Media(BaseModel, CustomBase):
    __tablename__ = "medias"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="title", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="description", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="url", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="education", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="education_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="experience", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="experience_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="accomplishment",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="accomplishment_id",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String)
    description = Column(Text)
    url = Column(String)

    # user profile
    user = relationship("User", back_populates="medias")
    user_id = Column(Integer, ForeignKey("users.id"))

    education = relationship("Education", back_populates="medias")
    education_id = Column(Integer, ForeignKey("educations.id"))

    experience = relationship("Experience", back_populates="medias")
    experience_id = Column(Integer, ForeignKey("experiences.id"))

    accomplishment = relationship("Accomplishment", back_populates="medias")
    accomplishment_id = Column(Integer, ForeignKey("accomplishments.id"))

    # events, posts, comments
    event = relationship("Event", back_populates="medias")
    event_id = Column(Integer, ForeignKey("events.id"))

    post = relationship("Post", back_populates="medias")
    post_id = Column(Integer, ForeignKey("posts.id"))

    comment = relationship("Comment", back_populates="medias")
    comment_id = Column(Integer, ForeignKey("comments.id"))

    message = relationship("Message", back_populates="medias")
    message_id = Column(Integer, ForeignKey("messages.id"))

    def __repr__(self):
        return f"Media({self.id} {self.title})"


class Group(BaseModel, CustomBase):
    __tablename__ = "groups"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="group_picture", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="name", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="description", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="users", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    group_picture = Column(String)
    name = Column(String, unique=True)
    description = Column(Text)

    users = relationship(
        "User", secondary="user_group", back_populates="groups", lazy="dynamic"
    )

    def __repr__(self):
        return f"Group({self.id} {self.name})"


class Event(BaseModel, CustomBase):
    __tablename__ = "events"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="body", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="timestamp", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="posts", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="event", lazy="dynamic")
    medias = relationship("Media", back_populates="event", lazy="dynamic")

    users = relationship(
        "User", secondary="user_event", back_populates="events", lazy="dynamic"
    )

    def __repr__(self):
        return f"Event({self.id}"


class Post(BaseModel, CustomBase):
    __tablename__ = "posts"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="body", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="timestamp", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="event", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="event_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="comments", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="posts")
    user_id = Column(Integer, ForeignKey("users.id"))

    event = relationship("Event", back_populates="posts")
    event_id = Column(Integer, ForeignKey("events.id"))

    comments = relationship("Comment", back_populates="post", lazy="dynamic")
    medias = relationship("Media", back_populates="post", lazy="dynamic")

    def __repr__(self):
        return f"Post({self.id})"


class Comment(BaseModel, CustomBase):
    __tablename__ = "comments"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="body", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="timestamp", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="user_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="post", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="post_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="comments")
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="comments")
    post_id = Column(Integer, ForeignKey("posts.id"))

    medias = relationship("Media", back_populates="comment", lazy="dynamic")

    def __repr__(self):
        return f"Comment({self.id})"


class Message(BaseModel, CustomBase):
    __tablename__ = "messages"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="body", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="timestamp", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="sender", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="sender_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="medias", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messagerecipients",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sender = relationship("User", back_populates="messages")
    sender_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("Media", back_populates="message", lazy="dynamic")

    messagerecipients = relationship(
        "MessageRecipient", back_populates="message", lazy="dynamic"
    )

    def __repr__(self):
        return f"Message({self.id})"


class MessageRecipient(BaseModel, CustomBase):
    __tablename__ = "messagerecipients"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="is_read", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="message", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="message_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="recipient", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="recipient_id", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messagegroup", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messagegroup_id",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)
    is_read = Column(Boolean)

    message = relationship("Message", back_populates="messagerecipients")
    message_id = Column(Integer, ForeignKey("messages.id"))

    recipient = relationship("User", back_populates="messagerecipients")
    recipient_id = Column(Integer, ForeignKey("users.id"))

    messagegroup = relationship("MessageGroup", back_populates="messagerecipients")
    messagegroup_id = Column(Integer, ForeignKey("messagegroups.id"))

    def __repr__(self):
        return f"MessageRecipient({self.id})"


class MessageGroup(BaseModel, CustomBase):
    __tablename__ = "messagegroups"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="name", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messagerecipients",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="users", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
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
        return f"MessageGroup({self.id} {self.name})"


class Notification(BaseModel, CustomBase):
    __tablename__ = "notifications"
    __serialization__ = [
        AttributeConfiguration(
            name="id", supports_dict=(False, True), supports_json=(False, True)
        ),
        AttributeConfiguration(
            name="name", supports_dict=(True, True), supports_json=(True, True)
        ),
        AttributeConfiguration(
            name="messagerecipients",
            supports_dict=(True, True),
            supports_json=(True, True),
        ),
        AttributeConfiguration(
            name="users", supports_dict=(True, True), supports_json=(True, True)
        ),
    ]
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String)

    users = relationship(
        "User",
        secondary="user_notification",
        back_populates="notifications",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"Notification({self.id} {self.name})"
