from json import loads
from logging import getLogger

from ya_tracker_client.domain.entities.checklist import Checklist, ChecklistCreate
from ya_tracker_client.domain.entities.deadline import Deadline
from ya_tracker_client.domain.repositories.base import EntityRepository


logger = getLogger(__name__)


class ChecklistRepository(EntityRepository):
    async def create_checklist_item(
        self,
        issue_id: str,
        text: str,
        checked: bool | None = None,
        assignee: str | None = None,
        deadline: Deadline | None = None,
    ) -> Checklist:
        """
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
        print(raw_response)
        return Checklist(**loads(raw_response))
