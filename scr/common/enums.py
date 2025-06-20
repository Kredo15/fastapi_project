import enum


class GenderEnum(enum.Enum):
    male = "мужской"
    female = "женский"


class FamilyStatusEnum(enum.Enum):
    not_married = ""
    dating = ""
    engaged = ""
    married = ""
    marriage = ""
    in_love = ""
    complicated = ""
    active_search = ""


class StatusEnum(enum.Enum):
    pending = "ожидание"
    accepted = "принято"
    rejected = "отклонено"


class PostsEnum(enum.Enum):
    text = "текст"
    photo = "фото"
    video = "видео"
    link = "ссылка"


class PrivacyGroupEnum(enum.Enum):
    public = "открытая"
    private = "закрытая"


class RoleGroupEnum(enum.Enum):
    member = "участник"
    moderator = "модератор"
    admin = "админ"


class PrivacyEnum(enum.Enum):
    public = "доступно всем"
    friends = "доступно друзьям"
    private = "только мне"


class TypeNotificationsEnum(enum.Enum):
    friend_request = "запрос в друзья"
    comment = "коммент"
    like = "лайк"
    group_invite = "приглашение в группу"
    event_invite = "приглашение на мероприятие"
    other = "другое"


class StatusEventsEnum(enum.Enum):
    attending = 'учавствую'
    interested = 'интересно'
    not_attending = 'не учавствую'
