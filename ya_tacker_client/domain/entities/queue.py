from pydantic import AliasChoices, Field

from ya_tacker_client.domain.entities.base import AbstractEntity


class Queue(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    key: str
    display: str
