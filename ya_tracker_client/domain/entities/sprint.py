from ya_tracker_client.domain.entities.base import AbstractEntity


class Sprint(AbstractEntity):
    url: str
    id: str
    display: str
