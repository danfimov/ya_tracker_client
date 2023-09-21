from datetime import datetime
from enum import Enum

from pydantic import AliasChoices, Field

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
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    inward: str
    outward: str


class IssueRelationship(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: int
    type: IssueRelationshipType
    direction: str
    object: IssueShort
    created_at: datetime = Field(validation_alias=AliasChoices("createdAt", "created_at"))
    updated_at: datetime = Field(validation_alias=AliasChoices("updatedAt", "updated_at"))
    created_by: UserShort = Field(validation_alias=AliasChoices("createdBy", "created_by"))
    updated_by: UserShort = Field(validation_alias=AliasChoices("updatedBy", "updated_by"))
    assignee: UserShort | None = None
    status: IssueStatus


class IssueRelationshipCreate(AbstractEntity):
    issue: str
    relationship: IssueRelationshipTypeEnum
