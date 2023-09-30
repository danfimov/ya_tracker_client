from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue_field import IssueFieldChange
from ya_tracker_client.domain.entities.queue import QueueShort


class Macro(AbstractEntity):
    url: str
    id: int
    queue: QueueShort
    name: str
    body: str
    field_changes: list[IssueFieldChange] = Field(default_factory=list)


class MacroCreate(AbstractEntity):
    name: str
    body: str | None = None
    field_changes: list[IssueFieldChange] | None = None


class MacroEdit(MacroCreate):
    pass
