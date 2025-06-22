from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from scr.common.enums import PrivacyEnum
from scr.common.base_model import Base, intpk, created_at, str_256
from scr.auth.models import UsersOrm
from scr.tag.models import TaggingsOrm


class PhotosOrm(Base):
    __tablename__ = 'tags'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(
        back_populates='photo'
    )
    album_id: Mapped[int] = mapped_column(
        ForeignKey('albums.id', ondelete="CASCADE")
    )
    album: Mapped['AlbumsOrm'] = relationship(
        back_populates='photo'
    )
    file_path: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[created_at]
    privacy: Mapped[PrivacyEnum]
    tagging: Mapped[list["TaggingsOrm"]] = relationship(back_populates='photo')


class AlbumsOrm(Base):
    __tablename__ = 'albums'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(
        back_populates='album'
    )
    photo: Mapped[list['PhotosOrm']] = relationship(
        back_populates='photo'
    )
    name: Mapped[str_256]
    description: Mapped[str]
    created_at: Mapped[created_at]
    privacy: Mapped[PrivacyEnum]


class VideosOrm(Base):
    __tablename__ = 'videos'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(
        back_populates='video'
    )
    name: Mapped[str_256]
    description: Mapped[str]
    file_path: Mapped[str]
    created_at: Mapped[created_at]
    privacy: Mapped[PrivacyEnum]
    tagging: Mapped[list["TaggingsOrm"]] = relationship(back_populates='video')
