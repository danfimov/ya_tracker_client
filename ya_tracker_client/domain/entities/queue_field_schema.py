from ya_tracker_client.domain.entities.base import AbstractEntity


class QueueFieldSchema(AbstractEntity):
    type: str  # TODO: "float" or "string" values - maybe better to replace with enum
    required: bool | None = None  # TODO: bool in documentation, but may be missing in response

    # TODO: documentation does not contain this fields
    items: str | None = None
