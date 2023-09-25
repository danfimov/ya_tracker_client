from datetime import date

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.queue import QueueShort


class QueueVersion(AbstractEntity):
    url: str
    id: int
    version: int
    queue: QueueShort
    name: str
    description: str | None = None  # TODO: string in documentation, but may be missing in response - TB145879
    start_date: date | None = None
    due_date: date | None = None
    released: bool
    archived: bool
