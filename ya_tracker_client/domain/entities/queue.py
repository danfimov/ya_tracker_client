from pydantic import AliasChoices, Field

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
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    key: str
    display: str


class QueueVersion(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: str
    display: str


class Queue(AbstractEntity):
    url: str = Field(validation_alias=AliasChoices("self", "url"))
    id: int
    key: str
    version: int
    name: str
    description: str | None = None  # TODO: string in documentation, but may be missing in response - TB145879
    lead: UserShort
    assign_auto: bool = Field(validation_alias=AliasChoices("assignAuto", "assign_auto"))
    default_type: IssueType = Field(validation_alias=AliasChoices("defaultType", "default_type"))
    default_priority: Priority = Field(validation_alias=AliasChoices("defaultPriority", "default_priority"))
    team_users: list[UserShort] = Field(default=list, validation_alias=AliasChoices("teamUsers", "team_users"))
    issue_types: list[IssueType] = Field(default=list, validation_alias=AliasChoices("issueTypes", "issue_types"))
    versions: list[QueueVersion] = Field(default=list)
    workflows: list[WorkflowShort] = Field(default=list)
    deny_voting: bool = Field(validation_alias=AliasChoices("denyVoting", "deny_voting"))
    issue_types_config: list[IssueTypeConfig] = Field(
        default=list,
        validation_alias=AliasChoices("issueTypesConfig", "issue_types_config"),
    )

    # TODO: documentation does not contain this fields - TB145879
    deny_conductor_autolink: bool = Field(
        validation_alias=AliasChoices("denyConductorAutolink", "deny_conductor_autolink"),
    )
    deny_tracker_auto_link: bool = Field(
        validation_alias=AliasChoices("denyTrackerAutolink", "deny_tracker_auto_link"),
    )
    use_component_permissions_intersection: bool = Field(
        validation_alias=AliasChoices("useComponentPermissionsIntersection", "use_component_permissions_intersection"),
    )
    workflow_actions_style: str = Field(
        validation_alias=AliasChoices("workflowActionsStyle", "workflow_actions_style"),
    )
    use_last_signature: bool = Field(
        validation_alias=AliasChoices("useLastSignature", "use_last_signature"),
    )


class QueueCreate(AbstractEntity):
    key: str
    name: str
    lead: str
    default_type: str
    default_priority: str = Field(
        validation_alias=AliasChoices("defaultPriority", "default_priority"),
    )
    issue_types_config: list[IssueTypeConfig] = Field(
        default=list,
        validation_alias=AliasChoices("issueTypesConfig", "issue_types_config"),
    )
