from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.issue_type import IssueType
from ya_tracker_client.domain.entities.resolution import ResolutionShort
from ya_tracker_client.domain.entities.workflow import WorkflowShort


class IssueTypeConfig(AbstractEntity):
    issue_type: IssueType
    workflow: WorkflowShort
    resolutions: list[ResolutionShort]
