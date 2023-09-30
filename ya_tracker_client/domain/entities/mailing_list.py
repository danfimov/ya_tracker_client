from ya_tracker_client.domain.entities.base import AbstractEntity


class MailingList(AbstractEntity):
    url: str
    id: str
    display: str
