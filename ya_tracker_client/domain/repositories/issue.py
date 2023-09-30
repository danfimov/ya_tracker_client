from ya_tracker_client.domain.entities.issue import Issue, IssueCreate, IssueEdit, IssueShort
from ya_tracker_client.domain.entities.issue_type import IssueType
from ya_tracker_client.domain.entities.priority import Priority
from ya_tracker_client.domain.entities.queue import QueueIdentifier
from ya_tracker_client.domain.entities.sprint import Sprint
from ya_tracker_client.domain.entities.transition import Transition
from ya_tracker_client.domain.entities.user import UserShort
from ya_tracker_client.domain.repositories.base import EntityRepository


class IssueRepository(EntityRepository):
    async def get_issue(self, issue_id: str) -> Issue:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-issue
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}",
        )
        return self._decode(raw_response, Issue)

    async def create_issue(
        self,
        summary: str,
        queue: QueueIdentifier | str | int,
        parent: IssueShort | str | None = None,
        description: str | None = None,
        sprint: list[Sprint | str] | None = None,
        issue_type: IssueType | None = None,
        priority: Priority | None = None,
        followers: list[UserShort | str] | None = None,
        assignee: list[UserShort | str] | None = None,
        unique: str | None = None,
        attachment_ids: list[str] | None = None,
    ) -> Issue:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/create-issue#queue
        """
        raw_response = await self._client.request(
            method="POST",
            uri="/issues/",
            payload=IssueCreate(
                summary=summary,
                queue=queue,
                parent=parent,
                description=description,
                sprint=sprint,
                type=issue_type,
                priority=priority,
                followers=followers,
                assignee=assignee,
                unique=unique,
                attachment_ids=attachment_ids,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Issue)

    async def edit_issue(
        self,
        issue_id: str,
        version: int | None = None,
        **kwargs,
    ) -> Issue:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/patch-issue
        """
        raw_response = await self._client.request(
            method="PATCH",
            uri=f"/issues/{issue_id}",
            params={"version": version} if version is not None else None,
            payload=IssueEdit(**kwargs).model_dump(exclude_unset=True),
        )
        return self._decode(raw_response, Issue)

    async def get_priorities(
        self,
        localized: bool = True,
    ) -> list[Priority]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-priorities
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/priorities/",
            params={"localized": str(localized)},
        )
        return self._decode(raw_response, Priority)

    async def get_issue_transitions(
        self,
        issue_id: str,
    ) -> list[Transition]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-transitions
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/transitions/",
        )
        return self._decode(raw_response, Transition, plural=True)
