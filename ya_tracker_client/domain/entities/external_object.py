from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.external_application import ExternalApplication


class ExternalObject(AbstractEntity):
    url: str
    id: str
    key: str
    application: ExternalApplication
