from ya_tracker_client.domain.entities.comment import Comment, CommentCreate, CommentEdit
from ya_tracker_client.domain.entities.user import UserShort
from ya_tracker_client.domain.repositories.base import EntityRepository


class CommentRepository(EntityRepository):
    async def add_comment(
        self,
        issue_id: str,
        text: str,
        attachment_ids: list[str] | None = None,
        summonees: list[str | UserShort] | None = None,
        maillist_summonees: list[str] | None = None,
        is_add_to_followers: bool = True,
    ) -> Comment:
        """
        Use this method to add a comment to an issue.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/add-comment
        """
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_id}/comments",
            payload=CommentCreate(
                text=text,
                attachment_ids=attachment_ids,
                summonees=summonees,
                maillist_summonees=maillist_summonees,
            ).model_dump(exclude_none=True, by_alias=True),
            params={"is_add_to_followers": str(is_add_to_followers).lower()},
        )
        return self._decode(raw_response, Comment)

    async def get_issue_comments(self, issue_id: str) -> list[Comment]:
        """
        Use this method to get a list of comments on an issue.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-comments
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/comments",
        )
        return self._decode(raw_response, Comment, plural=True)

    async def edit_comment(
        self,
        issue_id: str,
        comment_id: str | int,
        text: str,
        attachment_ids: list[str] | None = None,
    ) -> Comment:
        """
        Use this method to edit comments.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/edit-comment
        """
        raw_response = await self._client.request(
            method="PATCH",
            uri=f"/issues/{issue_id}/comments/{comment_id}",
            payload=CommentEdit(
                text=text,
                attachment_ids=attachment_ids,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Comment)

    async def delete_comment(
        self,
        issue_id: str,
        comment_id: str | int,
    ) -> None:
        """
        Use this method to delete issue comments.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/delete-comment
        """
        await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/comments/{comment_id}",
        )
