from pydantic import AliasChoices, Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue_status import IssueStatus


class Transition(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    to: IssueStatus
    display: str
