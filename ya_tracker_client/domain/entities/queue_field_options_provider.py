from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity


class QueueFieldOptionsProvider(AbstractEntity):
    type: str
    values: list = Field(default=list)
    defaults: list = Field(default=list)
