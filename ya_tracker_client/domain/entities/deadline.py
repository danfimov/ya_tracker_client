from datetime import datetime

from ya_tracker_client.domain.entities.base import AbstractEntity


class Deadline(AbstractEntity):
    date: datetime
    deadline_type: str = "date"
    is_exceeded: bool | None = None
