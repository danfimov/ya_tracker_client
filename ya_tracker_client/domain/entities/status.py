from pydantic import AliasChoices, Field

from ya_tracker_client.domain.entities.base import AbstractEntity


class Status(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    key: str
    display: str
