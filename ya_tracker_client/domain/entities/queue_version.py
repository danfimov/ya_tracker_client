from datetime import date

from pydantic import AliasChoices, Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.queue import QueueShort


class QueueVersion(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: int
    version: int
    queue: QueueShort
    name: str
    description: str | None = None  # TODO: string in documentation, but may be missing in response - TB145879
    start_date: date | None = Field(default=None, validation_alias=AliasChoices("startDate", "start_date"))
    due_date: date | None = Field(default=None, validation_alias=AliasChoices("dueDate", "due_date"))
    released: bool
    archived: bool
