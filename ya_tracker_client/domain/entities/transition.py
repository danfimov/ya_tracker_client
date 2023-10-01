from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue_status import IssueStatus


class Transition(AbstractEntity):
    url: str
    id: str
    to: IssueStatus
    display: str


class TransitionShort(AbstractEntity):
    url: str
    id: str
    display: str
