from datetime import datetime

from pydantic import BaseModel

from scr.common.enums import PrivacyGroupEnum, RoleGroupEnum
from scr.user.schemas import UsersSchema
from scr.content.schemas import PostsSchema


class GroupsAddSchema(BaseModel):
    name: str
    description: str
    creator_id: int
    privacy: PrivacyGroupEnum
    avatar: str


class GroupsSchema(GroupsAddSchema):
    id: int
    created_at: datetime


class GroupsRelSchema(GroupsSchema):
    creator: "UsersSchema"
    post: list["PostsSchema"]
    members: list["GroupMembersSchema"]


class GroupMembersAddSchema(BaseModel):
    group_id: int
    user_id: int
    role: RoleGroupEnum


class GroupMembersSchema(GroupMembersAddSchema):
    id: int
    join_date: datetime


class GroupMembersRelSchema(GroupMembersSchema):
    group: "GroupsSchema"
    user: "UsersSchema"
