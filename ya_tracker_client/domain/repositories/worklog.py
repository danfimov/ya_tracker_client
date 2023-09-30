from datetime import datetime

from ya_tracker_client.domain.entities.duration import Duration
from ya_tracker_client.domain.entities.worklog import Worklog, WorklogCreate, WorklogEdit
from ya_tracker_client.domain.repositories.base import EntityRepository


class WorklogRepository(EntityRepository):
    async def add_worklog_record(
        self,
        issue_id: str,
        start: datetime | str,
        duration: str,
        comment: str | None = None,
    ) -> Worklog:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/new-worklog
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_id}/worklog",
            payload=WorklogCreate(
                start=start,
                duration=duration,
                comment=comment,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Worklog)

    async def edit_worklog_record(
        self,
        issue_id: str,
        worklog_id: int | str,
        duration: str | Duration,
        comment: str | None = None,
    ) -> Worklog:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/patch-worklog
        """
        raw_response = await self._client.request(
            method="PATCH",
            uri=f"/issues/{issue_id}/worklog/{worklog_id}",
            payload=WorklogEdit(
                duration=duration,
                comment=comment,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Worklog)

    async def delete_worklog_record(
        self,
        issue_id: str,
        worklog_id: int | str,
    ) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/delete-worklog
        """
        await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/worklog/{worklog_id}",
        )

    async def get_worklog(self, issue_id: str) -> list[Worklog]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/issue-worklog
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/worklog",
        )
        return self._decode(raw_response, Worklog, plural=True)

    async def get_worklog_records_by_parameters(
        self,
        created_by: str | None = None,
        created_at_from: datetime | None = None,
        created_at_to: datetime | None = None,
    ) -> list[Worklog]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-worklog
        """
        payload = {}
        if created_by is not None:
            payload["createdBy"] = created_by
        if created_at_from is not None:
            payload["createdAt"] = {"from": created_at_from}
        if created_at_to is not None:
            if payload.get("createdAt") is None:
                payload["createdAt"]["to"] = created_at_to
            else:
                payload["createdAt"] = {"to": created_at_to}
        raw_response = await self._client.request(
            method="POST",
            uri="/worklog/_search",
            payload=payload,
        )
        return self._decode(raw_response, Worklog, plural=True)
