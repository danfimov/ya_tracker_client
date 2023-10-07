from datetime import datetime
from typing import Any

from pydantic import Field

from ya_tracker_client.domain.entities.attachment import AttachmentShort
from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.checklist import ChecklistItem
from ya_tracker_client.domain.entities.issue_status import IssueStatus
from ya_tracker_client.domain.entities.issue_type import IssueType
from ya_tracker_client.domain.entities.priority import Priority
from ya_tracker_client.domain.entities.queue import QueueIdentifier, QueueShort
from ya_tracker_client.domain.entities.sprint import Sprint
from ya_tracker_client.domain.entities.transition import TransitionShort
from ya_tracker_client.domain.entities.user import UserShort


class IssueShort(AbstractEntity):
    url: str
    id: str
    key: str
    display: str


class Issue(AbstractEntity):
    url: str
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
    created_at: datetime
    created_by: UserShort
    votes: int
    updated_at: datetime | None = None
    status: IssueStatus
    previous_status: IssueStatus | None = None
    direction: str | None = None

    transitions: list[TransitionShort] = Field(default_factory=list)
    attachments: list[AttachmentShort] = Field(default_factory=list)


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
    attachment_ids: list[str] | None = None


class IssueEdit(AbstractEntity):
    summary: str | None = None
    parent: IssueShort | str | None = None
    description: str | None = None
    sprint: list[Sprint | str] | None = None
    type: IssueType | None = None
    priority: Priority | None = None
    followers: list[UserShort | str] | None = None


class IssueWithChecklist(AbstractEntity):
    url: str
    id: str
    key: str
    version: int

    summary: str
    description: str | None = None
    type: IssueType
    priority: Priority
    followers: list[UserShort] | None = None
    queue: QueueShort
    favorite: bool
    assignee: UserShort | None = None

    last_comment_updated_at: datetime | None = None
    pending_reply_from: UserShort | None = None
    created_at: datetime
    updated_at: datetime
    created_by: UserShort
    updated_by: UserShort | None = None
    votes: int
    status: IssueStatus
    previous_status: IssueStatus | None = None
    status_start_time: datetime
    previous_status_last_assignee: UserShort | None = None
    deadline: datetime | None = None

    checklist_items: list[ChecklistItem] = Field(default_factory=list)


class IssueFindParameters(AbstractEntity):
    filter: dict[str, Any] | None = None
    query: str | None = None
    keys: str | None = None
    queue: str | None = None
