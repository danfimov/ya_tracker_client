from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.queue import QueueShort
from ya_tracker_client.domain.entities.user import UserShort


class Component(AbstractEntity):
    url: str
    id: int
    version: int
    name: str
    queue: QueueShort
    description: str
    lead: UserShort | None = None
    assign_auto: bool
