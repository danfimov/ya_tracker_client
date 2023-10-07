from ya_tracker_client.domain.entities.base import AbstractEntity


class IssueStatus(AbstractEntity):
    url: str
    id: str
    key: str
    display: str


class IssueStatusKey(AbstractEntity):
    key: str
