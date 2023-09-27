from ya_tracker_client.domain.entities.base import AbstractEntity


class WorkflowShort(AbstractEntity):
    url: str
    id: str
    key: str
    display: str
