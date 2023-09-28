from datetime import datetime

from pydantic import field_serializer

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.duration import Duration
from ya_tracker_client.domain.entities.issue import IssueShort
from ya_tracker_client.domain.entities.user import UserShort


class Worklog(AbstractEntity):
    url: str
    id: int
    version: int
    issue: IssueShort
    comment: str | None = None
    created_by: UserShort
    updated_by: UserShort | None
    created_at: datetime
    updated_at: datetime | None
    start: datetime
    duration: Duration

    @field_serializer("duration")
    def serialize_duration(self, duration: Duration):
        return str(duration)


class WorklogCreate(AbstractEntity):
    start: datetime
    duration: Duration
    comment: str | None = None

    @field_serializer("duration")
    def serialize_duration(self, duration: Duration):
        return str(duration)


class WorklogEdit(AbstractEntity):
    duration: Duration | None = None
    comment: str | None = None

    @field_serializer("duration")
    def serialize_duration(self, duration: Duration):
        return str(duration)
