from datetime import datetime

from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.external_object import ExternalObject
from ya_tracker_client.domain.entities.issue_relationship import IssueRelationshipType
from ya_tracker_client.domain.entities.user import UserShort


class ExternalLink(AbstractEntity):
    url: str
    id: int
    type: IssueRelationshipType
    direction: str = Field(examples=["outward", "inward"])
    object: ExternalObject
    created_by: UserShort
    updated_by: UserShort
    created_at: datetime
    updated_at: datetime
