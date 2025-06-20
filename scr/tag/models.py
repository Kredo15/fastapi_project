from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from scr.common.base_model import Base, intpk, str_256
from scr.content.models import PostsOrm
from scr.media.models import PhotosOrm, VideosOrm


class TagsOrm(Base):
    __tablename__ = 'tags'

    id: Mapped[intpk]
    name: Mapped[str_256]
    tagging: Mapped[list["TaggingsOrm"]] = relationship(back_populates='tag')


class TaggingsOrm(Base):
    __tablename__ = 'taggings'

    id: Mapped[intpk]
    tag_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id', ondelete="CASCADE")
    )
    tag: Mapped['TagsOrm'] = relationship(back_populates='tagging')
    post_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id', ondelete="CASCADE")
    )
    post: Mapped['PostsOrm'] = relationship(back_populates='tagging')
    photo_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id', ondelete="CASCADE")
    )
    photo: Mapped['PhotosOrm'] = relationship(back_populates='tagging')
    video_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id', ondelete="CASCADE")
    )
    video: Mapped['VideosOrm'] = relationship(back_populates='tagging')
