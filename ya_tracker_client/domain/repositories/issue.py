from json import loads

from ya_tracker_client.domain.entities.issue import Issue
from ya_tracker_client.domain.repositories.base import EntityRepository


class IssueRepository(EntityRepository):
    async def get_issue(self, issue_id: str) -> Issue:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/issues/get-issue

        :param issue_id: identifier of the issue.
        :return: issue DTO.
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}",
        )
        return Issue(**loads(raw_response))
