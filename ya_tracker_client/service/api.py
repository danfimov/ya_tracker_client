from ya_tracker_client.domain.repositories import (
    AttachmentRepository,
    ChecklistRepository,
    CommentRepository,
    ComponentRepository,
    IssueRelationshipRepository,
    IssueRepository,
    ProjectRepository,
    QueueRepository,
    UserRepository,
    WorklogRepository,
)
from ya_tracker_client.infrastructure.client import AiohttpClient


class YaTrackerClient(
    AttachmentRepository,
    CommentRepository,
    ChecklistRepository,
    ComponentRepository,
    IssueRelationshipRepository,
    IssueRepository,
    QueueRepository,
    UserRepository,
    WorklogRepository,
    ProjectRepository,
):
    def __init__(
        self,
        organisation_id: str | int,
        oauth_token: str | None = None,
        iam_token: str | None = None,
        api_host: str = "https://api.tracker.yandex.net",
        api_version: str = "v2",
        timeout: float = 0.,
    ) -> None:
        super().__init__(
            client=AiohttpClient(
                organisation_id=organisation_id,
                oauth_token=oauth_token,
                iam_token=iam_token,
                api_host=api_host,
                api_version=api_version,
                timeout=timeout,
            ),
        )
