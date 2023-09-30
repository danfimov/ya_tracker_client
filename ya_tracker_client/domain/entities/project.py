from datetime import date

from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.queue import QueueShort
from ya_tracker_client.domain.entities.user import UserShort


class ProjectCreate(AbstractEntity):
    name: str
    queues: str
    description: str | None = None
    lead: str | int | None = None
    status: str | None = Field(default=None, examples=["DRAFT", "IN_PROGRESS", "LAUNCHED", "POSTPONED"])
    start_date: date | None = None
    end_date: date | None = None


class Project(AbstractEntity):
    url: str
    id: int
    version: int
    key: str
    name: str
    description: str | None = None
    lead: UserShort
    status: str = Field(default=None, examples=["DRAFT", "IN_PROGRESS", "LAUNCHED", "POSTPONED"])
    start_date: date | None = None
    end_date: date | None = None


class ProjectWithQueues(Project):
    queues: list[QueueShort]


class ProjectEdit(AbstractEntity):
    name: str | None
    queues: str
    description: str | None = None
    lead: str | int | None = None
    status: str | None = Field(default=None, examples=["DRAFT", "IN_PROGRESS", "LAUNCHED", "POSTPONED"])
    start_date: date | None = None
    end_date: date | None = None
