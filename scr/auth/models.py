from pydantic import EmailStr
from sqlalchemy.orm import Mapped, mapped_column, relationship
from scr.common.base_model import Base, intpk, str_256, created_at, updated_at
from scr.profile.models import ProfileOrm
from scr.personal.models import FriendsOrm, MessagesOrm, NotificationsOrm
from scr.content.models import PostsOrm, CommentsOrm, LikesOrm
from scr.group.models import GroupsOrm, GroupMembersOrm
from scr.media.models import PhotosOrm, AlbumsOrm, VideosOrm
from scr.event.models import EventsOrm, EventMembersOrm


class UsersOrm(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    email: Mapped[EmailStr] = mapped_column(
        nullable=False, unique=True
    )
    username: Mapped[str_256] = mapped_column(
        nullable=False, unique=True
    )
    password: Mapped[str_256] = mapped_column(nullable=False)
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_administrator: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[created_at]
    last_login: Mapped[updated_at]
    profile: Mapped['ProfileOrm'] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    friend_requests_sent: Mapped[list['FriendsOrm']] = relationship(
        back_populates='requester', cascade='all, delete-orphan'
    )
    friend_requests_received: Mapped[list['FriendsOrm']] = relationship(
        back_populates='receiver', cascade='all, delete-orphan'
    )
    sender_message: Mapped[list['MessagesOrm']] = relationship(
        back_populates='sender', cascade='all, delete-orphan'
    )
    receiver_message: Mapped[list['MessagesOrm']] = relationship(
        back_populates='receiver', cascade='all, delete-orphan'
    )
    post: Mapped[list['PostsOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    comment: Mapped[list['CommentsOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    like: Mapped[list['LikesOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    created_group: Mapped[list['GroupsOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    group_member: Mapped[list['GroupMembersOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    photo: Mapped[list['PhotosOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    album: Mapped[list['AlbumsOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    video: Mapped[list['VideosOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    event: Mapped[list['EventsOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    creator_event: Mapped[list['EventsOrm']] = relationship(
        back_populates='creator', cascade='all, delete-orphan'
    )
    event_member: Mapped[list['EventMembersOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
    notification: Mapped[list['NotificationsOrm']] = relationship(
        back_populates='profile', cascade='all, delete-orphan'
    )
