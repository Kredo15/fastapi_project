from datetime import datetime, date

from pydantic import BaseModel, EmailStr

from scr.common.enums import GenderEnum, FamilyStatusEnum
from scr.personal.schemas import FriendsSchema, MessagesSchema, NotificationsSchema
from scr.media.schemas import PhotosSchema, AlbumsSchema, VideosSchema
from scr.content.schemas import PostsSchema, CommentsSchema, LikeSchema
from scr.group.schemas import GroupsSchema, GroupMembersSchema
from scr.event.schemas import EventsSchema, EventMembersSchema


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


class ProfileAddSchema(BaseModel):
    user_id: int
    gender: GenderEnum | None
    date_of_birth: date
    photo: str | None
    city: str | None
    country: str | None
    family_status: FamilyStatusEnum | None
    additional_information: str | None


class ProfileSchema(ProfileAddSchema):
    id: int


class ProfileRelSchema(ProfileAddSchema):
    user: "UsersSchema"


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
