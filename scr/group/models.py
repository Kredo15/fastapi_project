from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from scr.common.enums import PrivacyGroupEnum, RoleGroupEnum
from scr.common.base_model import Base, intpk, str_256, created_at
from scr.auth.models import UsersOrm
from scr.content.models import PostsOrm


class GroupsOrm(Base):
    __tablename__ = 'groups'

    id: Mapped[intpk]
    name: Mapped[str_256]
    description: Mapped[str]
    creator_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    creator: Mapped['UsersOrm'] = relationship(back_populates='created_group')
    created_at: Mapped[created_at]
    privacy: Mapped[PrivacyGroupEnum]
    avatar: Mapped[str]
    post: Mapped[list['PostsOrm']] = relationship(
        back_populates='group', cascade='all, delete-orphan'
    )
    members: Mapped[list['GroupMembersOrm']] = relationship(
        back_populates='group', cascade='all, delete-orphan'
    )


class GroupMembersOrm(Base):
    __tablename__ = 'group_members'

    id: Mapped[intpk]
    group_id: Mapped[int] = mapped_column(
        ForeignKey('groups.id', ondelete="CASCADE")
    )
    group: Mapped['GroupsOrm'] = relationship(back_populates='members')
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='group_member')
    role: Mapped[RoleGroupEnum]
    join_date: Mapped[created_at]
