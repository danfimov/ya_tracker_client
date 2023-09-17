from ya_tacker_client.domain.repositories.issue import IssueRepository
from ya_tacker_client.infrastructure.client import AiohttpClient


class YaTrackerClient(IssueRepository):
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
