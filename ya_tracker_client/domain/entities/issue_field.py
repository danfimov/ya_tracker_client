from ya_tracker_client.domain.entities.base import AbstractEntity


class IssueFieldShort(AbstractEntity):
    url: str
    id: str
    display: str


class IssueFieldChange(AbstractEntity):
    field: IssueFieldShort
    value: list
