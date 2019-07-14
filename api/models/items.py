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
from datetime import datetime


class Payment(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="payments")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("MediaPayment", back_populates="payment", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class Experience(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    employer = Column(String)
    location = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    is_currently_work_here = Column(Boolean)
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="experiences")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship(
        "MediaExperience", back_populates="experience", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class Education(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    education_type = Column(String)
    degree = Column(String)
    field_of_study = Column(String, default="no_field_of_study")
    school = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

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
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="skills")
    user_id = Column(Integer, ForeignKey("users.id"))

    medias = relationship("MediaSkill", back_populates="skill", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class OrganizationGroup(BaseModel, ModelSerializerMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    users = relationship("User", back_populates="organizationgroup", lazy="dynamic")
    medias = relationship(
        "MediaOrganizationGroup", back_populates="organizationgroup", lazy="dynamic"
    )

    communications = relationship(
        "Communication",
        secondary="organizationgroup_communication",
        back_populates="organizationgroups",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Communication(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    description = Column(Text)
    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    author = relationship("User", back_populates="communications")
    author_id = Column(Integer, ForeignKey("users.id"))

    organizationgroups = relationship(
        "OrganizationGroup",
        secondary="organizationgroup_communication",
        back_populates="communications",
        lazy="dynamic",
    )
    medias = relationship(
        "MediaCommunication",
        back_populates="communication",
        lazy="dynamic",
    )
    comments = relationship(
        "Comment", back_populates="communication", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Comment(BaseModel, ModelSerializerMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(String, default="no_body")
    timestamp = Column(DateTime, default=datetime.utcnow)

    author = relationship("User", back_populates="comments")
    author_id = Column(Integer, ForeignKey("users.id"))

    communication = relationship(
        "Communication", back_populates="comments"
    )
    communication_id = Column(Integer, ForeignKey("communications.id"))

    medias = relationship(
        "MediaComment", back_populates="comment", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.body}, id = {self.id})"


##############################################################################
##############################################################################
#   Below here are not used classes  #
##############################################################################
##############################################################################


class Group(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    description = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

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
    timestamp = Column(DateTime, default=datetime.utcnow)

    users = relationship(
        "User", secondary="user_event", back_populates="events", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class Message(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

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
    timestamp = Column(DateTime, default=datetime.utcnow)

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
    timestamp = Column(DateTime, default=datetime.utcnow)

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
    timestamp = Column(DateTime, default=datetime.utcnow)

    users = relationship(
        "User",
        secondary="user_notification",
        back_populates="notifications",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"
