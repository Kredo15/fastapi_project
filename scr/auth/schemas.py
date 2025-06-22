from datetime import datetime

from pydantic import BaseModel, EmailStr

from scr.profile.schemas import ProfileSchema
from scr.personal.schemas import FriendsSchema, MessagesSchema, NotificationsSchema
from scr.media.schemas import PhotosSchema, AlbumsSchema, VideosSchema
from scr.content.schemas import PostsSchema, CommentsSchema, LikeSchema
from scr.group.schemas import GroupsSchema, GroupMembersSchema
from scr.event.schemas import EventsSchema, EventMembersSchema


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    username: str | None = None


class UsersAddSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str


class UsersSchema(UsersAddSchema):
    id: int
    active: bool
    is_verified: bool
    is_administrator: bool
    created_at: datetime
    last_login: datetime


class UsersRelSchema(UsersSchema):
    profile: "ProfileSchema"
    friend_requests_sent: list["FriendsSchema"]
    friend_requests_received: list["FriendsSchema"]
    sender_message: list["MessagesSchema"]
    receiver_message: list["MessagesSchema"]
    post: list["PostsSchema"]
    comment: list["CommentsSchema"]
    like: list["LikeSchema"]
    created_group: list["GroupsSchema"]
    group_member: list["GroupMembersSchema"]
    photo: list["PhotosSchema"]
    album: list["AlbumsSchema"]
    video: list["VideosSchema"]
    event: list["EventsSchema"]
    creator_event: list["EventsSchema"]
    event_member: list["EventMembersSchema"]
    notification: list["NotificationsSchema"]
