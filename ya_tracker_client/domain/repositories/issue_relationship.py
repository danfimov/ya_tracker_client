from json import loads

from ya_tracker_client.domain.entities.issue_relationship import (
    IssueRelationship,
    IssueRelationshipCreate,
    IssueRelationshipTypeEnum,
)
from ya_tracker_client.domain.repositories.base import EntityRepository


class IssueRelationshipRepository(EntityRepository):
    async def create_issue_relationship(
        self,
        issue_from: str,
        issue_to: str,
        relationship: IssueRelationshipTypeEnum,
    ) -> IssueRelationship:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/issues/link-issue
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_from}/links",
            payload=IssueRelationshipCreate(
                issue=issue_to,
                relationship=relationship,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return IssueRelationship(**loads(raw_response))

    async def get_issue_relationships(
        self,
        issue_id: str,
    ) -> list[IssueRelationship]:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/issues/get-links
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/links",
        )
        return [IssueRelationship(**raw_issue_relationship) for raw_issue_relationship in loads(raw_response)]

    async def delete_issue_relationships(
        self,
        issue_id: str,
        link_id: int,
    ) -> None:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/issues/delete-link-issue
        """
        await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/links/{link_id}",
        )
