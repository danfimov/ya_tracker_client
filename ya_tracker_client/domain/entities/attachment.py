from datetime import datetime

from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.user import UserShort


class AttachmentMetadata(AbstractEntity):
    size: str


class Attachment(AbstractEntity):
    url: str
    id: int
    name: str
    content: str
    thumbnail: str | None = None
    created_by: UserShort
    created_at: datetime
    mimetype: str = Field(..., examples=["text/plain", "image/png"])
    size: int
    metadata: AttachmentMetadata | None = None


class AttachmentShort(AbstractEntity):
    url: str
    id: int
    display: str
