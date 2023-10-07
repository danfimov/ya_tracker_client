from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue_status import IssueStatus, IssueStatusKey


class Action(AbstractEntity):
    type: str = Field(examples=["Transition", "Update", "Event.comment-create", "Webhook", "CalculateFormula"])
    id: int | str | None = None
    status: IssueStatus | IssueStatusKey | None = None
