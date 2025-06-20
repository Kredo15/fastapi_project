from datetime import datetime

from pydantic import BaseModel

from scr.common.enums import PrivacyEnum
from scr.user.schemas import UsersSchema


class PhotosAddSchema(BaseModel):
    user_id: int
    album_id: int
    file_path: str
    description: str
    privacy: PrivacyEnum


class PhotosSchema(PhotosAddSchema):
    id: int
    created_at: datetime


class PhotosRelSchema(PhotosSchema):
    user: "UsersSchema"
    album: "AlbumsSchema"
    tagging: list[""]


class AlbumsAddSchema(BaseModel):
    user_id: int
    name: str
    description: str
    privacy: PrivacyEnum


class AlbumsSchema(AlbumsAddSchema):
    id: int
    created_at: datetime


class AlbumsRelSchema(AlbumsSchema):
    user: "UsersSchema"
    photo: list["PhotosSchema"]


class VideosAddSchema(BaseModel):
    user_id: int
    name: str
    description: str
    file_path: str
    privacy: PrivacyEnum


class VideosSchema(VideosAddSchema):
    id: int
    created_at: datetime


class VideosRelSchema(VideosSchema):
    user: "UsersSchema"
    tagging: list[""]
