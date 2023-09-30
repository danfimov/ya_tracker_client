from ya_tracker_client.domain.entities.component import Component
from ya_tracker_client.domain.repositories.base import EntityRepository


class ComponentRepository(EntityRepository):
    async def get_components(self) -> list[Component]:
        """
        YT docs: https://cloud.yandex.com/en/docs/tracker/get-components
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/components",
        )
        return self._decode(raw_response, Component, plural=True)
