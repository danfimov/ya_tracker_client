from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.queue_field_category import QueueFieldCategory
from ya_tracker_client.domain.entities.queue_field_options_provider import QueueFieldOptionsProvider
from ya_tracker_client.domain.entities.queue_field_query_provider import QueueFieldQueryProvider
from ya_tracker_client.domain.entities.queue_field_schema import QueueFieldSchema
from ya_tracker_client.domain.entities.queue_field_suggest_provider import QueueFieldSuggestProvider


class QueueField(AbstractEntity):
    url: str
    id: str
    name: str
    version: int
    field_schema: QueueFieldSchema = Field(alias="schema")
    readonly: bool
    options: bool
    suggest: bool
    options_provider: QueueFieldOptionsProvider | None = None  # TODO: not required in response - not documented
    query_provider: QueueFieldQueryProvider | None = None
    order: int

    # TODO: documentation does not contain this fields
    suggest_provider: QueueFieldSuggestProvider | None = None
    type: str
    category: QueueFieldCategory
