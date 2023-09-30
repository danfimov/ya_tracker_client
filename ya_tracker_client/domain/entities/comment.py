from datetime import datetime

from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.mailing_list import MailingList
from ya_tracker_client.domain.entities.user import UserShort


class Comment(AbstractEntity):
    url: str
    id: int
    long_id: str
    text: str
    created_by: UserShort
    created_at: datetime
    updated_by: UserShort
    updated_at: datetime
    summonees: list[UserShort] = Field(default_factory=list)
    maillistsummonees: list[MailingList] = Field(default_factory=list)
    version: int
    type: str = Field(examples=["standard", "incoming", "outcoming"])
    transport: str = Field(examples=["internal", "email"])


class CommentCreate(AbstractEntity):
    text: str
    attachment_ids: list[str] | None = None
    summonees: list[UserShort | str] | None = None
    maillistsummonees: list[str] | None = None


class CommentEdit(AbstractEntity):
    text: str
    attachment_ids: list[str] | None = None
