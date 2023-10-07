from ya_tracker_client.domain.entities.external_application import ExternalApplication
from ya_tracker_client.domain.entities.external_link import ExternalLink
from ya_tracker_client.domain.repositories.base import EntityRepository


class ExternalLinkRepository(EntityRepository):
    async def get_external_applications(self) -> list[ExternalApplication]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-applications
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/applications",
        )
        return self._decode(raw_response, ExternalApplication, plural=True)

    async def get_external_links(self, issue_id: str) -> list[ExternalLink]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-external-links
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/remotelinks",
        )
        return self._decode(raw_response, ExternalLink, plural=True)

    async def add_external_link(
        self,
        issue_id: str,
        key: str,
        origin: str,
        relationship: str = "RELATES",
        backlink: bool = False,
    ) -> ExternalLink:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/add-external-link
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_id}/remotelinks",
            payload={
                "key": key,
                "origin": origin,
                "relationship": relationship,
            },
            params={"backlink": str(backlink).lower()},
        )
        return self._decode(raw_response, ExternalLink)

    async def delete_external_link(self, issue_id: str, external_link_id: str | int) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/delete-external-link
        """
        await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/remotelinks/{external_link_id}",
        )
