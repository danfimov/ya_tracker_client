from pydantic import AliasChoices, Field

from ya_tracker_client.domain.entities.base import AbstractEntity


class Priority(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    key: str
    display: str | None = None
    version: int | None = None
    name: str | dict | None = None
    order: int | None = None
