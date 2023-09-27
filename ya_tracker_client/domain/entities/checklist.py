from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.deadline import Deadline


class ChecklistCreate(AbstractEntity):
    text: str
    checked: bool | None = None
    assignee: str | None = None
    deadline: Deadline | None = None


class Checklist(AbstractEntity):
    ...


class IssueWithoutChecklist(AbstractEntity):
    url: str
    id: str
    key: str
    version: int
