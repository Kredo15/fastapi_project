from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from scr.common.enums import StatusEnum, TypeNotificationsEnum
from scr.common.base_model import Base, intpk, created_at, updated_at
from scr.user.models import UsersOrm
from scr.content.models import PostsOrm
from scr.group.models import GroupsOrm
from scr.event.models import EventsOrm


class FriendsOrm(Base):
    __tablename__ = 'friends'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    requester: Mapped['UsersOrm'] = relationship(back_populates='friend_requests_sent')
    friend_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    receiver: Mapped['UsersOrm'] = relationship(back_populates='friend_requests_received')
    status: Mapped[StatusEnum] = mapped_column(default=StatusEnum.pending)
    request_date: Mapped[created_at]
    acceptance_date: Mapped[updated_at]


class MessagesOrm(Base):
    __tablename__ = 'messages'

    id: Mapped[intpk]
    sender_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    sender: Mapped['UsersOrm'] = relationship(back_populates='sender_message')
    receiver_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    receiver: Mapped['UsersOrm'] = relationship(back_populates='receiver_message')
    content: Mapped[str]
    created_at: Mapped[created_at]
    is_read: Mapped[bool] = mapped_column(default=False)


class NotificationsOrm(Base):
    __tablename__ = 'notifications'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='notification')
    type: Mapped[TypeNotificationsEnum]
    content: Mapped[str]
    is_read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[created_at]
    sent_request_user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    sent_request_user: Mapped['UsersOrm'] = relationship(
        back_populates='sent_request')
    post_id: Mapped[int] = mapped_column(
        ForeignKey('posts.id', ondelete="CASCADE")
    )
    post: Mapped['PostsOrm'] = relationship(
        back_populates='notification'
    )
    group_id: Mapped[int] = mapped_column(
        ForeignKey('groups.id', ondelete="CASCADE")
    )
    group: Mapped['GroupsOrm'] = relationship(
        back_populates='notification'
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey('events.id', ondelete="CASCADE")
    )
    event: Mapped['EventsOrm'] = relationship(
        back_populates='notification'
    )
