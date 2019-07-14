from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    Text,
    ForeignKey,
    Date,
    Column,
)
from sqlalchemy.orm import relationship
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import base64
import os


class User(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    # database only
    password_hash = Column(String)
    role = Column(String, default="normal_user")

    # on create or login
    token = Column(String, unique=True)
    token_expiration = Column(DateTime)

    # database only - should be many to many
    privilege = Column(String, default="normal_privilege")

    # intro
    first_name = Column(String)
    last_name = Column(String, default="no_name")
    profession = Column(String)
    sex = Column(String)
    summary = Column(Text)
    country = Column(String)
    birthday = Column(Date)
    address = Column(String)
    # should be one to many:
    phone = Column(String)
    email = Column(String, unique=True)
    website = Column(String)

    # status
    application_status = Column(String, default="blank")
    payment_status = Column(String, default="blank")

    # activity
    is_active = Column(Boolean)
    last_active = Column(DateTime)

    # dates
    register_date = Column(DateTime, default=datetime.utcnow)
    application_date = Column(DateTime)
    reapplication_date = Column(DateTime)
    rebutted_date = Column(DateTime)
    send_payment_date = Column(DateTime)
    resend_payment_date = Column(DateTime)
    rebutted_payment_date = Column(DateTime)
    accepted_date = Column(DateTime)
    rejected_date = Column(DateTime)

    # comment nga administratori
    comment_from_administrator = Column(Text)

    # many to one
    organizationgroup = relationship("OrganizationGroup", back_populates="users")
    organizationgroup_id = Column(Integer, ForeignKey("organizationgroups.id"))

    # intro - one to many
    medias = relationship("MediaUser", back_populates="user", lazy="dynamic")

    # experiences, educations, skills, payments
    experiences = relationship("Experience", back_populates="user", lazy="dynamic")
    educations = relationship("Education", back_populates="user", lazy="dynamic")
    skills = relationship("Skill", back_populates="user", lazy="dynamic")
    payments = relationship("Payment", back_populates="user", lazy="dynamic")

    # official communications
    communications = relationship(
        "Communication", back_populates="author", lazy="dynamic"
    )
    # official comments
    comments = relationship(
        "Comment", back_populates="author", lazy="dynamic"
    )

    # database related one to many
    posts = relationship("Post", back_populates="author", lazy="dynamic")
    comments = relationship("Comment", back_populates="author", lazy="dynamic")
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
