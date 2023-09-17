from pydantic import AliasChoices, Field

from ya_tacker_client.domain.entities.base import AbstractEntity


class Sprint(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    display: str
