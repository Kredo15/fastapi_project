from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from scr.common.enums import PostsEnum
from scr.common.base_model import Base, intpk, created_at, updated_at
from scr.user.models import UsersOrm
from scr.tag.models import TaggingsOrm
from scr.group.models import GroupsOrm


class PostsOrm(Base):
    __tablename__ = 'posts'

    id: Mapped[intpk]
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='post')
    group_id: Mapped[int] = mapped_column(
        ForeignKey('groups.id', ondelete="CASCADE")
    )
    group: Mapped['GroupsOrm'] = relationship(back_populates='post')
    image_path: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    post_type: Mapped[PostsEnum]
    image_url: Mapped[str]
    video_url: Mapped[str]
    link_url: Mapped[str]
    like: Mapped[list['LikesOrm']] = relationship(
        back_populates='post', cascade='all, delete-orphan'
    )
    likes_count: Mapped[int] = mapped_column(default=0)
    comment: Mapped[list['CommentsOrm']] = relationship(
        back_populates='post', cascade='all, delete-orphan'
    )
    comments_count: Mapped[int] = mapped_column(default=0)
    shared_count: Mapped[int] = mapped_column(default=0)
    is_public: Mapped[bool]
    tagging: Mapped[list['TaggingsOrm']] = relationship(
        back_populates='post', cascade='all, delete-orphan'
    )


class CommentsOrm(Base):
    __tablename__ = 'comments'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='comment')
    post_id: Mapped[int] = mapped_column(
        ForeignKey('posts.id', ondelete="CASCADE")
    )
    post: Mapped['PostsOrm'] = relationship(back_populates='comment')
    content: Mapped[str]
    created_at: Mapped[created_at]
    like: Mapped[list['LikesOrm']] = relationship(back_populates='comment')


class LikesOrm(Base):
    __tablename__ = 'likes'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='like')
    post_id: Mapped[int] = mapped_column(
        ForeignKey('posts.id', ondelete="CASCADE")
    )
    post: Mapped['PostsOrm'] = relationship(back_populates='like')
    comment_id: Mapped[int] = mapped_column(
        ForeignKey('comments.id', ondelete="CASCADE")
    )
    comment: Mapped['CommentsOrm'] = relationship(back_populates='like')
    created_at: Mapped[created_at]
