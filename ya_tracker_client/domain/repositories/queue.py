from ya_tracker_client.domain.entities.action import Action
from ya_tracker_client.domain.entities.calendar import Calendar
from ya_tracker_client.domain.entities.issue_type_config import IssueTypeConfig
from ya_tracker_client.domain.entities.queue import Queue, QueueCreate
from ya_tracker_client.domain.entities.queue_autoaction import Autoaction, AutoactionCreate
from ya_tracker_client.domain.entities.queue_field import QueueField
from ya_tracker_client.domain.entities.queue_version import QueueVersion
from ya_tracker_client.domain.entities.trigger import Trigger, TriggerCondition, TriggerCreate
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
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/create-queue
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
        return self._decode(raw_response, Queue)

    async def get_queue(self, queue_id: str | int) -> Queue:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/get-queue
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}",
        )
        return self._decode(raw_response, Queue)

    async def get_queues(self) -> list[Queue]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/get-queues
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/queues/",
        )
        return self._decode(raw_response, Queue, plural=True)

    async def get_queue_versions(self, queue_id: str | int) -> list[QueueVersion]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/get-versions
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/versions",
        )
        return self._decode(raw_response, QueueVersion, plural=True)

    async def get_queue_fields(self, queue_id: str | int) -> list[QueueField]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/get-fields
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/fields",
        )
        return self._decode(raw_response, QueueField, plural=True)

    async def delete_queue(self, queue_id: str | int) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/delete-queue
        """
        await self._client.request(
            method="DELETE",
            uri=f"/queues/{queue_id}",
        )

    async def restore_queue(self, queue_id: str | int) -> Queue:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/restore-queue
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/queues/{queue_id}/_restore",
        )
        return self._decode(raw_response, Queue)

    async def delete_tag_in_queue(self, queue_id: str | int, tag_name: str) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/delete-tag
        """
        await self._client.request(
            method="DELETE",
            uri=f"/queues/{queue_id}/tags/_remove",
            payload={"tag": tag_name},
        )

    async def create_autoaction(
        self,
        queue_id: str | int,
        name: str,
        actions: list[Action],
        issue_filter: list[dict] | dict | None = None,
        query: str | None = None,
        active: bool | None = None,
        enable_notifications: bool | None = None,
        interval_millis: int = 3_600_000,
        calendar: Calendar | None = None,
    ) -> Autoaction:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/create-autoaction
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/queues/{queue_id}/autoactions",
            payload=AutoactionCreate(
                name=name,
                actions=actions,
                filter=issue_filter,
                query=query,
                active=active,
                enable_notifications=enable_notifications,
                interval_millis=interval_millis,
                calendar=calendar,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Autoaction)

    async def get_autoaction(
        self,
        queue_id: str | int,
        autoaction_id: str | int,
    ) -> Autoaction:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/get-autoaction
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/autoactions/{autoaction_id}",
        )
        return self._decode(raw_response, Autoaction)

    async def get_autoactions(
        self,
        queue_id: str | int,
    ) -> list[Autoaction]:
        # TODO: add info about this handler to YC docs
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/autoactions/",
        )
        return self._decode(raw_response, Autoaction, plural=True)

    async def delete_autoaction(
        self,
        queue_id: str | int,
        autoaction_id: str | int,
    ) -> None:
        # TODO: add info about this handler to YC docs
        await self._client.request(
            method="DELETE",
            uri=f"/queues/{queue_id}/autoactions/{autoaction_id}",
        )

    async def create_trigger(
        self,
        queue_id: str | int,
        name: str,
        actions: list[Action],
        conditions: list[TriggerCondition] | None = None,
        active: bool | None = None,
    ) -> Trigger:
        raw_response = await self._client.request(
            method="POST",
            uri=f"/queues/{queue_id}/triggers",
            payload=TriggerCreate(
                name=name,
                actions=actions,
                conditions=conditions,
                active=active,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Trigger)

    async def get_trigger(self, queue_id: str | int, trigger_id: str | int) -> Trigger:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/queues/get-trigger
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/triggers/{trigger_id}",
        )
        return self._decode(raw_response, Trigger)

    async def get_triggers(self, queue_id: str | int) -> list[Trigger]:
        # TODO: add info about this handler to YC docs
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/triggers/",
        )
        return self._decode(raw_response, Trigger, plural=True)

    async def delete_trigger(self, queue_id: str | int, trigger_id: str | int) -> None:
        # TODO: add info about this handler to YC docs
        await self._client.request(
            method="DELETE",
            uri=f"/queues/{queue_id}/triggers/{trigger_id}",
        )
