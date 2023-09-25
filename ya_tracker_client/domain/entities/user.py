from datetime import datetime

from ya_tracker_client.domain.entities.base import AbstractEntity


class UserShort(AbstractEntity):
    url: str
    id: str
    display: str


class User(AbstractEntity):
    url: str
    uid: int
    login: str
    tracker_uid: int
    passport_uid: int
    cloud_uid: str | None = None
    first_name: str
    last_name: str
    display: str
    email: str
    external: bool
    has_licence: bool | None = None
    dismissed: bool
    user_new_filters: bool | None = None
    disable_notifications: bool
    first_login_date: datetime | None = None
    last_login_date: datetime | None = None
    welcome_mail_sent: bool | None = None
