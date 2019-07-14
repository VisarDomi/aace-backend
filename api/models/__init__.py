from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Table,
    Column,
)
from ..common.database import BaseModel


organizationgroup_officialcommunication = Table(
    "organizationgroup_officialcommunication",
    BaseModel.metadata,
    Column("organizationgroup_id", Integer, ForeignKey("organizationgroups.id")),
    Column(
        "officialcommunication_id", Integer, ForeignKey("officialcommunications.id")
    ),
)

##############################################################################
# Non used many to many tables                                               #
##############################################################################
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
