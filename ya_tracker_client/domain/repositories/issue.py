from typing import Any

from ya_tracker_client.domain.entities.issue import Issue, IssueCreate, IssueEdit, IssueFindParameters, IssueShort
from ya_tracker_client.domain.entities.issue_change_history import IssueChangeHistory, IssueChangeHistoryParameters
from ya_tracker_client.domain.entities.issue_type import IssueType
from ya_tracker_client.domain.entities.priority import Priority
from ya_tracker_client.domain.entities.queue import QueueIdentifier
from ya_tracker_client.domain.entities.sprint import Sprint
from ya_tracker_client.domain.entities.transition import Transition
from ya_tracker_client.domain.entities.user import UserShort
from ya_tracker_client.domain.repositories.base import EntityRepository


class IssueRepository(EntityRepository):
    async def get_issue(self, issue_id: str, expand: str = "") -> Issue:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-issue
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}",
            params={"expand": expand},
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
            params={"localized": str(localized).lower()},
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

    async def move_issue_to_another_queue(
        self,
        issue_id: str,
        queue_id: str,
        notify: bool = True,
        notify_author: bool = False,
        move_all_fields: bool = False,
        initial_status: bool = False,
        expand: str | None = None,
        **kwargs,
    ) -> Issue:
        """
        Move an issue to a different queue.

        Before executing the method, make sure the user has permission
        to edit the issues to be moved and is allowed to create them in
        the new queue.

        Warning!
        If an issue you want to move has a type and status that are
        missing in the target queue, no transfer will be made. To reset
        the issue status to the initial value when moving it, use the
        InitialStatus parameter.

        By default, when an issue is moved, the values of its
        components, versions, and projects are cleared. If the new queue
        has the same values of the fields specified, use the
        MoveAllFields parameter to move the components, versions, and
        projects.

        If the issue has the local field values specified, they will be
        reset when moving the issue to a different queue.

        You can use the kwargs if you need to change the
        parameters of the issue being moved. The kwargs has the
        same format as when editing issues.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/move-issue
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_id}/_move",
            params={
                "queue": queue_id,
                "notify": str(notify).lower(),
                "notifyAuthor": str(notify_author).lower(),
                "moveAllFields": str(move_all_fields).lower(),
                "initialStatus": str(initial_status).lower(),
                "expand": expand or "",
            },
            payload=IssueEdit(**kwargs).model_dump(exclude_unset=True),
        )
        return self._decode(raw_response, Issue)

    async def find_number_of_issues(self, issue_filter: dict[str, Any] | None = None, query: str | None = None) -> int:
        """
        Use this method to find out how many issues meet the criteria in your request.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/count-issues
        """
        raw_response = await self._client.request(
            method="POST",
            uri="/issues/_count",
            payload={
                "filter": issue_filter,
                "query": query,
            },
        )
        return int(raw_response)

    async def release_scroll_view_resources(self, scroll_id: str, scroll_token: str) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/search-release

        :param scroll_id: ID of the page with scroll results. The ID value is taken from the `X-Scroll-Id` header of the response to the search for issues request.
        :param scroll_token: token that certifies that the request belongs to the current user. The ID value is taken from the `X-Scroll-Token` header of the response to the search for issues request.
        :return: None
        """  # noqa: E501
        await self._client.request(
            method="POST",
            uri="/system/search/scroll/_clear",
            payload={scroll_id: scroll_token},
        )

    async def make_status_transition(
        self,
        issue_id: str,
        transition_id: int | str,
        comment: str,
        **kwargs,
    ) -> list[Transition]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/new-transition
        """
        payload = {"comment": comment}
        payload.update(kwargs)
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_id}/transitions/{transition_id}/_execute",
            payload=payload,
        )
        return self._decode(raw_response, Transition, plural=True)

    async def get_history_issue_changes(
        self,
        issue_id: str,
        change_id: str | None = None,
        per_page: int = 50,
        field: str | None = None,
        change_type: str | None = None,
    ) -> list[IssueChangeHistory]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-changelog
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/changelog",
            payload=IssueChangeHistoryParameters(
                id=change_id,
                per_page=per_page,
                field=field,
                type=change_type,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, IssueChangeHistory, plural=True)

    async def find_issues(
        self,
        issue_filter: dict[str, str] | None = None,
        query: str | None = None,
        order: str | None = None,
        expand: str | None = None,
        keys: str | None = None,
        queue: str | None = None,
    ) -> list[Issue]:
        params = {}
        if order:
            params["order"] = order
        if expand:
            params["expand"] = expand

        raw_response = await self._client.request(
            method="POST",
            uri="/issues/_search",
            params=params,
            payload=IssueFindParameters(
                filter=issue_filter,
                query=query,
                keys=keys,
                queue=queue,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Issue, plural=True)
