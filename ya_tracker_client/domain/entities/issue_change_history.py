from datetime import datetime

from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue import IssueShort
from ya_tracker_client.domain.entities.issue_field import IssueFieldShort
from ya_tracker_client.domain.entities.user import UserShort


class FieldChangeHistoryState(AbstractEntity):
    id: str
    url: str
    key: str
    display: str


class FieldChangeHistory(AbstractEntity):
    field: IssueFieldShort
    change_from: FieldChangeHistoryState | str | list | None = Field(default=None, alias="from")
    change_to: FieldChangeHistoryState | str | list | None = Field(default=None, alias="to")


class IssueChangeHistory(AbstractEntity):
    id: str
    url: str
    issue: IssueShort
    updated_at: datetime
    updated_by: UserShort
    transport: str
    type: str
    fields: list[FieldChangeHistory] = Field(default_factory=list)


class IssueChangeHistoryParameters(AbstractEntity):
    id: str | None = None
    per_page: int = 50
    field: str | None = None
    type: str | None = None
