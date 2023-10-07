from ya_tracker_client.domain.entities.bulk_operation import BulkChange, BulkChangeStatus, BulkMove, BulkOperation
from ya_tracker_client.domain.repositories.base import EntityRepository


class BulkOperationRepository(EntityRepository):
    async def bulk_move_issues(
        self,
        queue_id: str,
        issue_ids: list[str],
        values: dict | None = None,
        move_all_fields: bool | None = None,
        initial_status: bool | None = None,
        notify: bool = False,
    ) -> BulkOperation:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/bulkchange/bulk-move-issues
        """
        raw_response = await self._client.request(
            method="POST",
            uri="/bulkchange/_move",
            payload=BulkMove(
                queue=queue_id,
                issues=issue_ids,
                values=values,
                move_all_fields=move_all_fields,
                initial_status=initial_status,
            ).model_dump(exclude_none=True, by_alias=True),
            params={"notify": str(notify).lower()},
        )
        return self._decode(raw_response, BulkOperation)

    async def bulk_change_issues(
        self,
        issue_ids: list[str],
        values: dict,
        notify: bool = False,
    ) -> BulkOperation:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/bulkchange/bulk-update-issues
        """
        raw_response = await self._client.request(
            method="POST",
            uri="/bulkchange/_update",
            payload=BulkChange(
                issues=issue_ids,
                values=values,
            ).model_dump(exclude_none=True, by_alias=True),
            params={"notify": str(notify).lower()},
        )
        return self._decode(raw_response, BulkOperation)

    async def bulk_change_issues_statuses(
        self,
        issue_ids: list[str],
        transition_id: str,
        values: dict | None = None,
        notify: bool = False,
    ) -> BulkOperation:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/bulkchange/bulk-transition
        """
        raw_response = await self._client.request(
            method="POST",
            uri="/bulkchange/_transition",
            payload=BulkChangeStatus(
                transition=transition_id,
                issues=issue_ids,
                values=values,
            ).model_dump(exclude_none=True, by_alias=True),
            params={"notify": str(notify).lower()},
        )
        return self._decode(raw_response, BulkOperation)
