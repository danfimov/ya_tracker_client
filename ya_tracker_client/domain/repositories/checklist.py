from ya_tracker_client.domain.entities.checklist import ChecklistCreate, ChecklistItem, ChecklistItemEdit
from ya_tracker_client.domain.entities.deadline import Deadline
from ya_tracker_client.domain.entities.issue import IssueWithChecklist
from ya_tracker_client.domain.repositories.base import EntityRepository


class ChecklistRepository(EntityRepository):
    async def create_checklist_item(
        self,
        issue_id: str,
        text: str,
        checked: bool | None = None,
        assignee: str | None = None,
        deadline: Deadline | None = None,
    ) -> IssueWithChecklist:
        """
        Use this request to create a checklist and add new items to it.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/add-checklist-item
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_id}/checklistItems",
            payload=ChecklistCreate(
                text=text,
                checked=checked,
                assignee=assignee,
                deadline=deadline,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, IssueWithChecklist)

    async def get_checklist_items(self, issue_id: str) -> list[ChecklistItem]:
        """
        Use this request to get the parameters of an issue's checklist.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-checklist
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/checklistItems",
        )
        return self._decode(raw_response, ChecklistItem, plural=True)

    async def edit_checklist_item(
        self,
        issue_id: str,
        checklist_item_id: str,
        text: str,
        checked: bool | None = None,
        assignee: str | None = None,
        deadline: Deadline | None = None,
    ) -> IssueWithChecklist:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/edit-checklist
        """
        raw_response = await self._client.request(
            method="PATCH",
            uri=f"/issues/{issue_id}/checklistItems/{checklist_item_id}",
            payload=ChecklistItemEdit(
                text=text,
                checked=checked,
                assignee=assignee,
                deadline=deadline,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, IssueWithChecklist)

    async def delete_checklist(self, issue_id: str) -> IssueWithChecklist:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/delete-checklist
        """
        raw_response = await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/checklistItems",
        )
        return self._decode(raw_response, IssueWithChecklist)

    async def delete_checklist_item(self, issue_id: str, checklist_item_id: str):
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/delete-checklist-item
        """
        raw_response = await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/checklistItems/{checklist_item_id}",
        )
        return self._decode(raw_response, IssueWithChecklist)
