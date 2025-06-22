from datetime import datetime

from pydantic import BaseModel

from scr.common.enums import StatusEnum, TypeNotificationsEnum
from scr.auth.schemas import UsersSchema


class FriendsAddSchema(BaseModel):
    user_id: int
    friend_id: int
    status: StatusEnum


class FriendsSchema(FriendsAddSchema):
    id: int
    request_date: datetime
    acceptance_date: datetime


class FriendsRelSchema(FriendsSchema):
    requester: "UsersSchema"
    receiver: "UsersSchema"


class MessagesAddSchema(BaseModel):
    sender_id: int
    receiver_id: int
    content: str


class MessagesSchema(MessagesAddSchema):
    id: int
    created_at: datetime
    is_read: bool


class MessagesRelSchema(MessagesSchema):
    sender: "UsersSchema"
    receiver: "UsersSchema"


class NotificationsAddSchema(BaseModel):
    user_id: int
    type: TypeNotificationsEnum
    content: str
    sent_request_user_id: int
    post_id: int | None
    group_id: int | None
    event_id: int | None


class NotificationsSchema(NotificationsAddSchema):
    id: int
    is_read: bool
    created_at: datetime


class NotificationsRelSchema(NotificationsSchema):
    user: "UsersSchema"
    sent_request_user: "UsersSchema"
    post: ""
    group: ""
    event: ""
