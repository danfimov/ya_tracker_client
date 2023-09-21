from datetime import datetime

from pydantic import AliasChoices, Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue_type import IssueType
from ya_tracker_client.domain.entities.priority import Priority
from ya_tracker_client.domain.entities.queue import QueueIdentifier, QueueShort
from ya_tracker_client.domain.entities.sprint import Sprint
from ya_tracker_client.domain.entities.status import Status
from ya_tracker_client.domain.entities.user import UserShort


class IssueShort(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    key: str
    display: str


class Issue(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    key: str
    version: int

    summary: str
    parent: IssueShort | None = None
    description: str | None = None
    sprint: list[Sprint] | None = None
    type: IssueType
    priority: Priority
    followers: list[UserShort] | None = None
    queue: QueueShort
    previous_queue: QueueShort | None = None
    favorite: bool
    assignee: UserShort | None = None

    last_comment_update_at: datetime | None = None
    aliases: list[str] | None = None
    updated_by: UserShort | None = None
    created_at: datetime = Field(validation_alias=AliasChoices("createdAt", "created_at"))
    created_by: UserShort = Field(validation_alias=AliasChoices("createdBy", "created_by"))
    votes: int
    updated_at: datetime | None = None
    status: Status
    previous_status: Status | None = None
    direction: str | None = None


class IssueCreate(AbstractEntity):
    summary: str
    queue: QueueIdentifier | str | int
    parent: IssueShort | str | None = None
    description: str | None = None
    sprint: list[Sprint | str] | None = None
    type: IssueType | None = None
    priority: Priority | None = None
    followers: list[UserShort | str] | None = None
    assignee: list[UserShort | str] | None = None
    unique: str | None = None
    attachment_ids: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices("attachmentIds", "attachment_ids"),
    )


class IssueEdit(AbstractEntity):
    summary: str | None = None
    parent: IssueShort | str | None = None
    description: str | None = None
    sprint: list[Sprint | str] | None = None
    type: IssueType | None = None
    priority: Priority | None = None
    followers: list[UserShort | str] | None = None
