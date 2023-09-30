from ya_tracker_client.domain.entities.issue_field import IssueFieldChange
from ya_tracker_client.domain.entities.macro import Macro, MacroCreate, MacroEdit
from ya_tracker_client.domain.repositories.base import EntityRepository


class MacroRepository(EntityRepository):
    async def get_macros(self, queue_id: str) -> list[Macro]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/get-macroses
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/macros",
        )
        return self._decode(raw_response, Macro, plural=True)

    async def get_macro(self, queue_id: str, macro_id: str) -> Macro:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/get-macros
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/queues/{queue_id}/macros/{macro_id}",
        )
        return self._decode(raw_response, Macro)

    async def create_macro(
        self,
        queue_id: str,
        name: str,
        body: str | None = None,
        field_changes: list[IssueFieldChange] | None = None,
    ) -> Macro:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/post-macros
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/queues/{queue_id}/macros",
            payload=MacroCreate(
                name=name,
                body=body,
                field_changes=field_changes,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Macro)

    async def edit_macro(
        self,
        queue_id: str,
        macro_id: str,
        name: str,
        body: str | None = None,
        field_changes: list[IssueFieldChange] | None = None,
    ) -> Macro:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/patch-macros
        """
        raw_response = await self._client.request(
            method="PATCH",
            uri=f"/queues/{queue_id}/macros/{macro_id}",
            payload=MacroEdit(
                name=name,
                body=body,
                field_changes=field_changes,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Macro)

    async def delete_macro(self, queue_id: str, macro_id: str) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/delete-macros
        """
        await self._client.request(
            method="DELETE",
            uri=f"/queues/{queue_id}/macros/{macro_id}",
        )
