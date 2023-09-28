from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.deadline import Deadline
from ya_tracker_client.domain.entities.user import UserShort


class ChecklistCreate(AbstractEntity):
    text: str
    checked: bool | None = None
    assignee: str | None = None
    deadline: Deadline | None = None


class ChecklistItem(AbstractEntity):
    id: str
    text: str
    text_html: str
    checked: bool
    checklist_item_type: str
    deadline: Deadline | None = None
    assignee: UserShort | None = None


class ChecklistItemEdit(AbstractEntity):
    text: str
    checked: bool | None = None
    assignee: str | None = None
    deadline: Deadline | None = None
