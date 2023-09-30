from ya_tracker_client.domain.entities.base import AbstractEntity


class ExternalApplication(AbstractEntity):
    url: str
    id: str
    type: str
    name: str
