from json import loads
from typing import Any, Type

from pydantic import BaseModel

from ya_tracker_client.infrastructure.client import BaseClient


class DeserializationMixin:
    @staticmethod
    def _decode(
        value: bytes,
        return_type: Type[BaseModel] | None = None,
        plural: bool = False,
    ) -> Any:
        if plural:
            return [return_type(**raw_item) for raw_item in loads(value)]
        return return_type(**loads(value))


class EntityRepository(DeserializationMixin):
    def __init__(self, client: BaseClient) -> None:
        self._client = client
        super().__init__()

    async def stop(self) -> None:
        await self._client.stop()
