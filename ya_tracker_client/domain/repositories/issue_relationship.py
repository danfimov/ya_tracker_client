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
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/link-issue
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_from}/links",
            payload=IssueRelationshipCreate(
                issue=issue_to,
                relationship=relationship,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, IssueRelationship)

    async def get_issue_relationships(
        self,
        issue_id: str,
    ) -> list[IssueRelationship]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-links
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/links",
        )
        return self._decode(raw_response, IssueRelationship, plural=True)

    async def delete_issue_relationships(
        self,
        issue_id: str,
        link_id: int,
    ) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/delete-link-issue
        """
        await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/links/{link_id}",
        )
