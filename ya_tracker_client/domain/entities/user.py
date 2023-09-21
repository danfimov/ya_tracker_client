from datetime import datetime

from pydantic import AliasChoices, Field

from ya_tracker_client.domain.entities.base import AbstractEntity


class UserShort(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    display: str


class User(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    uid: int
    login: str
    tracker_uid: int = Field(validation_alias=AliasChoices("trackerUid", "tracker_uid"))
    passport_uid: int = Field(validation_alias=AliasChoices("passportUid", "passport_uid"))
    cloud_uid: str | None = Field(
        default=None,
        validation_alias=AliasChoices("cloudUid", "cloud_uid"),
    )
    first_name: str = Field(validation_alias=AliasChoices("firstName", "first_name"))
    last_name: str = Field(validation_alias=AliasChoices("lastName", "last_name"))
    display: str
    email: str
    external: bool
    has_licence: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("hasLicence", "has_licence"),
    )
    dismissed: bool
    user_new_filters: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("userNewFilters", "user_new_filters"),
    )
    disable_notifications: bool = Field(validation_alias=AliasChoices("disableNotifications", "disable_notifications"))
    first_login_date: datetime | None = Field(
        default=None,
        validation_alias=AliasChoices("firstLoginDate", "first_login_date"),
    )
    last_login_date: datetime | None = Field(
        default=None,
        validation_alias=AliasChoices("lastLoginDate", "last_login_date"),
    )
    welcome_mail_sent: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("welcomeMailSent", "welcome_mail_sent"),
    )
