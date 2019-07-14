from sqlalchemy import (
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
    Column,
)
from sqlalchemy.orm import relationship
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin
from datetime import datetime


class MediaUser(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="medias")
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaPayment(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    payment = relationship("Payment", back_populates="medias")
    payment_id = Column(Integer, ForeignKey("payments.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaExperience(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

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
    timestamp = Column(DateTime, default=datetime.utcnow)

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
    timestamp = Column(DateTime, default=datetime.utcnow)

    skill = relationship("Skill", back_populates="medias")
    skill_id = Column(Integer, ForeignKey("skills.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaOrganizationGroup(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    organizationgroup = relationship("OrganizationGroup", back_populates="medias")
    organizationgroup_id = Column(Integer, ForeignKey("organizationgroups.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaOfficialCommunication(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    officialcommunication = relationship(
        "OfficialCommunication", back_populates="medias"
    )
    officialcommunication_id = Column(Integer, ForeignKey("officialcommunications.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"


class MediaOfficialComment(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, default="no_title")
    description = Column(Text)
    filename = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    officialcomment = relationship("OfficialComment", back_populates="medias")
    officialcomment_id = Column(Integer, ForeignKey("officialcomments.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, id = {self.id})"
