from ya_tracker_client.domain.client import BaseClient


class EntityRepository:
    def __init__(self, client: BaseClient) -> None:
        self._client = client
        super().__init__()

    async def stop(self) -> None:
        await self._client.stop()
