from datetime import datetime

from pydantic import model_validator

from ya_tracker_client.domain.entities.action import Action
from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.calendar import Calendar
from ya_tracker_client.domain.entities.queue import QueueShort


class Autoaction(AbstractEntity):
    id: int | str
    url: str
    queue: str | QueueShort
    name: str
    version: int
    active: bool
    created: datetime
    updated: datetime
    filter: list[dict] | dict | None = None
    query: str | None = None
    actions: list[Action]
    enable_notifications: bool
    total_issues_processed: int
    interval_millis: int
    calendar: dict[str, int] | None = None


class AutoactionCreate(AbstractEntity):
    name: str
    filter: list[dict] | dict | None = None
    query: str | None = None
    actions: list[Action]
    active: bool | None = None
    enable_notifications: bool | None = None
    interval_millis: int = 3_600_000
    calendar: Calendar | None = None

    @model_validator(mode="after")
    def filter_or_query_is_exists(self) -> "AutoactionCreate":
        if self.filter is None and self.query is None:
            raise ValueError("Filter or query must be not None")
        return self
