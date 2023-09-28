from pydantic import Field

from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue_type import IssueType
from ya_tracker_client.domain.entities.issue_type_config import IssueTypeConfig
from ya_tracker_client.domain.entities.priority import Priority
from ya_tracker_client.domain.entities.user import UserShort
from ya_tracker_client.domain.entities.workflow import WorkflowShort


class QueueIdentifier(AbstractEntity):
    id: str
    key: str


class QueueShort(AbstractEntity):
    url: str
    id: str
    key: str
    display: str


class QueueVersion(AbstractEntity):
    url: str
    id: str
    display: str


class Queue(AbstractEntity):
    url: str
    id: int
    key: str
    version: int
    name: str
    description: str | None = None  # TODO: string in documentation, but may be missing in response - TB145879
    lead: UserShort
    assign_auto: bool
    default_type: IssueType
    default_priority: Priority
    team_users: list[UserShort] = Field(default_factory=list)
    issue_types: list[IssueType] = Field(default_factory=list)
    versions: list[QueueVersion] = Field(default_factory=list)
    workflows: list[WorkflowShort] = Field(default_factory=list)
    deny_voting: bool
    issue_types_config: list[IssueTypeConfig] = Field(default_factory=list)

    # TODO: documentation does not contain this fields - TB145879
    deny_conductor_autolink: bool | None = None
    deny_tracker_auto_link: bool | None = None
    use_component_permissions_intersection: bool | None = None
    workflow_actions_style: str | None = None
    use_last_signature: bool | None = None


class QueueCreate(AbstractEntity):
    key: str
    name: str
    lead: str
    default_type: str
    default_priority: str
    issue_types_config: list[IssueTypeConfig] = Field(default_factory=list)
