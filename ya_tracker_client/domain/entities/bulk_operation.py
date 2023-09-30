from datetime import datetime

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.user import UserShort


class BulkOperation(AbstractEntity):
    id: str
    url: str
    created_by: UserShort
    created_at: datetime
    status: str
    status_text: str
    execution_chunk_percent: int
    execution_issue_percent: int


class BulkMove(AbstractEntity):
    queue: str
    issues: list[str]
    values: dict | None = None
    move_all_fields: bool | None = None
    initial_status: bool | None = None


class BulkChange(AbstractEntity):
    issues: list[str]
    values: dict


class BulkChangeStatus(AbstractEntity):
    issues: list[str]
    transition: str
    values: dict | None = None
