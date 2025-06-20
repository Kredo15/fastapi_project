from datetime import datetime, date

from pydantic import BaseModel

from scr.common.enums import PrivacyEnum, StatusEventsEnum
from scr.user.schemas import UsersSchema
from scr.group.schemas import GroupsSchema


class EventsAddSchema(BaseModel):
    user_id: int
    creator_id: int
    group_id: int | None
    name: str
    description: str
    start_date: date
    end_date: date
    location: str
    privacy: PrivacyEnum


class EventsSchema(EventsAddSchema):
    id: int
    created_at: datetime


class EventsRelSchema(EventsSchema):
    user: "UsersSchema"
    creator: "UsersSchema"
    group: "GroupsSchema"
    event_member: list["EventMembersSchema"]


class EventMembersAddSchema(BaseModel):
    event_id: int
    user_id: int
    status: StatusEventsEnum


class EventMembersSchema(EventMembersAddSchema):
    id: int
    created_at: datetime


class EventMembersRelSchema(EventMembersSchema):
    event: "EventsSchema"
    user: "UsersSchema"
