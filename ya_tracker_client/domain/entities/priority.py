from ya_tracker_client.domain.entities.base import AbstractEntity


class Priority(AbstractEntity):
    url: str
    id: int
    key: str
    display: str | None = None
    version: int | None = None
    name: str | dict | None = None
    order: int | None = None
