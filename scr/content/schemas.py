from datetime import datetime

from pydantic import BaseModel

from scr.common.enums import PostsEnum
from scr.user.schemas import UsersSchema


class PostsAddSchema(BaseModel):
    content: str
    user_id: int | None
    group_id: int | None
    image_path: str
    post_type: PostsEnum
    image_url: str | None
    video_url: str | None
    link_url: str | None
    is_public: bool


class PostsSchema(PostsAddSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    likes_count: int
    comments_count: int
    shared_count: int


class PostsRelSchema(PostsSchema):
    user: "UsersSchema"
    group: ""
    tagging: list[""]


class CommentsAddSchema(BaseModel):
    user_id: int
    post_id: int
    content: str | None


class CommentsSchema(CommentsAddSchema):
    id: int
    created_at: datetime


class CommentsRelSchema(CommentsSchema):
    user: "UsersSchema"
    post: "PostsSchema"
    like: list["LikeSchema"]


class LikeAddSchema(BaseModel):
    user_id: int
    post_id: int | None
    comment_id: int | None


class LikeSchema(LikeAddSchema):
    id: int
    created_at: datetime


class LikeRelSchema(LikeSchema):
    user: "UsersSchema"
    post: "PostsSchema"
    comment: "CommentsSchema"
