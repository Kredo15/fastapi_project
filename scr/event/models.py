import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from scr.common.enums import PrivacyEnum, StatusEventsEnum
from scr.common.base_model import Base, intpk, str_256, created_at
from scr.user.models import UsersOrm
from scr.group.models import GroupsOrm


class EventsOrm(Base):
    __tablename__ = 'events'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='event')
    creator_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    creator: Mapped['UsersOrm'] = relationship(back_populates='creator_event')
    group_id: Mapped[int] = mapped_column(
        ForeignKey('groups.id', ondelete="CASCADE")
    )
    group: Mapped['GroupsOrm'] = relationship(back_populates='event')
    name: Mapped[str_256]
    description: Mapped[str]
    start_date: Mapped[datetime.date]
    end_date: Mapped[datetime.date]
    location: Mapped[str_256]
    privacy: Mapped[PrivacyEnum]
    created_at: Mapped[created_at]
    event_member: Mapped[list['EventMembersOrm']] = relationship(
        back_populates='event', cascade='all, delete-orphan'
    )


class EventMembersOrm(Base):
    __tablename__ = 'event_members'

    id: Mapped[intpk]
    event_id: Mapped[int] = mapped_column(
        ForeignKey('events.id', ondelete="CASCADE"),  primary_key=True,
    )
    event: Mapped['EventsOrm'] = relationship(back_populates='event_member')
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE"),  primary_key=True,
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='event_member')
    status: Mapped[StatusEventsEnum]
    created_at: Mapped[created_at]
