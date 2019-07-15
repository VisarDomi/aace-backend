from sqlalchemy import Integer, ForeignKey, Table, Column
from ..common.database import BaseModel


organizationgroup_communication = Table(
    "organizationgroup_communication",
    BaseModel.metadata,
    Column("organizationgroup_id", Integer, ForeignKey("organizationgroups.id")),
    Column("communication_id", Integer, ForeignKey("communications.id")),
)

organizationgroup_event = Table(
    "organizationgroup_event",
    BaseModel.metadata,
    Column("organizationgroup_id", Integer, ForeignKey("organizationgroups.id")),
    Column("event_id", Integer, ForeignKey("events.id")),
)

organizationgroup_poll = Table(
    "organizationgroup_poll",
    BaseModel.metadata,
    Column("organizationgroup_id", Integer, ForeignKey("organizationgroups.id")),
    Column("poll_id", Integer, ForeignKey("polls.id")),
)

user_option = Table(
    "user_option",
    BaseModel.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("option_id", Integer, ForeignKey("options.id")),
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

user_messagegroup = Table(
    "user_messagegroup",
    BaseModel.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("messagegroup_id", Integer, ForeignKey("messagegroups.id")),
)
