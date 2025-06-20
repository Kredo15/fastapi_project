from pydantic import BaseModel

from scr.content.schemas import PostsSchema
from scr.media.schemas import PhotosSchema, VideosSchema


class TagsAddSchema(BaseModel):
    name: str


class TagsSchema(TagsAddSchema):
    id: int


class TagsRelSchema(TagsSchema):
    tagging: list["TaggingsSchema"]


class TaggingsAddSchema(BaseModel):
    tag_id: int
    post_id: int | None
    photo_id: int | None
    video_id: int | None


class TaggingsSchema(TaggingsAddSchema):
    id: int


class TaggingsRelSchema(TaggingsSchema):
    tag: "TagsSchema"
    post: "PostsSchema"
    photo: "PhotosSchema"
    video: "VideosSchema"
