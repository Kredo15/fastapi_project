import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from scr.common.base_model import Base, intpk, str_256
from scr.common.enums import GenderEnum, FamilyStatusEnum
from scr.auth.models import UsersOrm


class ProfileOrm(Base):
    __tablename__ = 'profile'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE")
    )
    user: Mapped['UsersOrm'] = relationship(back_populates='profile')
    gender: Mapped[GenderEnum]
    date_of_birth: Mapped[datetime.date]
    photo: Mapped[str]
    city: Mapped[str_256]
    country: Mapped[str_256]
    family_status: Mapped[FamilyStatusEnum]
    additional_information: Mapped[str]
