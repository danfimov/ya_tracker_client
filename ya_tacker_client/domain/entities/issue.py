from datetime import datetime

from pydantic import AliasChoices, Field

from ya_tacker_client.domain.entities.base import AbstractEntity
from ya_tacker_client.domain.entities.priority import Priority
from ya_tacker_client.domain.entities.queue import Queue
from ya_tacker_client.domain.entities.sprint import Sprint
from ya_tacker_client.domain.entities.status import Status
from ya_tacker_client.domain.entities.user import User


class IssueShort(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    key: str
    display: str


class IssueType(AbstractEntity):
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
    followers: list[User] | None = None
    queue: Queue
    previous_queue: Queue | None = None
    favorite: bool
    assignee: User | None = None

    last_comment_update_at: datetime | None = None
    aliases: list[str] | None = None
    updated_by: User | None = None
    created_at: datetime = Field(validation_alias=AliasChoices("createdAt", "created_at"))
    created_by: User = Field(validation_alias=AliasChoices("createdBy", "created_by"))
    votes: int
    updated_at: datetime | None = None
    status: Status
    previous_status: Status | None = None
    direction: str | None = None
