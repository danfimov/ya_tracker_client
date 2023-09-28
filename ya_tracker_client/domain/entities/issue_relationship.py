from datetime import datetime
from enum import Enum

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue import IssueShort
from ya_tracker_client.domain.entities.issue_status import IssueStatus
from ya_tracker_client.domain.entities.user import UserShort


class IssueRelationshipTypeEnum(str, Enum):
    RELATES = "relates"
    IS_DEPENDENT_BY = "is dependent by"
    DEPENDS_ON = "depends on"
    IS_SUBTASK_FOR = "is subtask for"
    IS_PARENT_TASK_FOR = "is parent task for"
    DUPLICATES = "duplicates"
    IS_DUPLICATED_BY = "is duplicated by"
    IS_EPIC_OF = "is epic of"
    HAS_EPIC = "has epic"


class IssueRelationshipType(AbstractEntity):
    url: str
    id: str
    inward: str
    outward: str


class IssueRelationship(AbstractEntity):
    url: str
    id: int
    type: IssueRelationshipType
    direction: str
    object: IssueShort
    created_at: datetime
    updated_at: datetime
    created_by: UserShort
    updated_by: UserShort
    assignee: UserShort | None = None
    status: IssueStatus


class IssueRelationshipCreate(AbstractEntity):
    issue: str
    relationship: IssueRelationshipTypeEnum
