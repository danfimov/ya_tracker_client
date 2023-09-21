from json import loads

from ya_tracker_client.domain.entities.issue_type_config import IssueTypeConfig
from ya_tracker_client.domain.entities.queue import Queue, QueueCreate
from ya_tracker_client.domain.entities.queue_field import QueueField
from ya_tracker_client.domain.entities.queue_version import QueueVersion
from ya_tracker_client.domain.repositories.base import EntityRepository


class QueueRepository(EntityRepository):
    async def create_queue(
        self,
        key: str,
        name: str,
        lead: str,
        default_type: str,
        default_priority: str,
        issue_types_config: list[IssueTypeConfig],
    ) -> Queue:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/create-queue
        """
        raw_response = await self._client.request(
            method="POST",
            uri="/queues/",
            payload=QueueCreate(
                key=key,
                name=name,
                lead=lead,
                default_type=default_type,
                default_priority=default_priority,
                issue_types_config=issue_types_config,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return Queue(**loads(raw_response))

    async def get_queue(self, queue_id: str | int) -> Queue:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/get-queue
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}",
        )
        return Queue(**loads(raw_response))

    async def get_queues(self) -> list[Queue]:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/get-queues
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/queues/",
        )
        return [Queue(**raw_queue) for raw_queue in loads(raw_response)]

    async def get_queue_versions(self, queue_id: str | int) -> list[QueueVersion]:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/get-versions
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/versions",
        )
        return [QueueVersion(**raw_queue_version) for raw_queue_version in loads(raw_response)]

    async def get_queue_fields(self, queue_id: str | int) -> list[QueueField]:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/get-fields
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/fields",
        )
        for raw_queue_field in loads(raw_response):
            print(*raw_queue_field.items(), sep="\n")
            print()
            QueueField(**raw_queue_field)

        return [QueueField(**raw_queue_field) for raw_queue_field in loads(raw_response)]

    async def delete_queue(self, queue_id: str | int) -> None:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/delete-queue
        """
        await self._client.request(
            method="DELETE",
            uri=f"/queues/{queue_id}",
        )

    async def restore_queue(self, queue_id: str | int) -> Queue:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/restore-queue
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/queues/{queue_id}/_restore",
        )
        return Queue(**loads(raw_response))

    async def delete_tag_in_queue(self, queue_id: str | int, tag_name: str) -> None:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/concepts/queues/delete-tag
        """
        await self._client.request(
            method="DELETE",
            uri=f"/queues/{queue_id}/tags/_remove",
            payload={"tag": tag_name},
        )
