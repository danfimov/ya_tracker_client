from pydantic import AliasChoices, Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.queue_field_category import QueueFieldCategory
from ya_tracker_client.domain.entities.queue_field_options_provider import QueueFieldOptionsProvider
from ya_tracker_client.domain.entities.queue_field_query_provider import QueueFieldQueryProvider
from ya_tracker_client.domain.entities.queue_field_schema import QueueFieldSchema
from ya_tracker_client.domain.entities.queue_field_suggest_provider import QueueFieldSuggestProvider


class QueueField(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    name: str
    version: int
    field_schema: QueueFieldSchema = Field(
        validation_alias=AliasChoices("schema"),
    )
    readonly: bool
    options: bool
    suggest: bool
    options_provider: QueueFieldOptionsProvider | None = Field(  # TODO: not required in response - not documented
        default=None, validation_alias=AliasChoices("optionsProvider", "options_provider"),
    )
    query_provider: QueueFieldQueryProvider | None = Field(
        default=None, validation_alias=AliasChoices("queryProvider", "query_provider"),
    )
    order: int

    # TODO: documentation does not contain this fields
    suggest_provider: QueueFieldSuggestProvider | None = Field(
        default=None, validation_alias=AliasChoices("suggestProvider", "suggest_provider"),
    )
    type: str
    category: QueueFieldCategory
