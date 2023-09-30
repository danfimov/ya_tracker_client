from typing import BinaryIO

from aiohttp import FormData

from ya_tracker_client.domain.entities.attachment import Attachment
from ya_tracker_client.domain.repositories.base import EntityRepository


class AttachmentRepository(EntityRepository):
    async def get_attachments_list(self, issue_id: str) -> list[Attachment]:
        """
        Use this method to get a list of files attached to an issue and to comments below it.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-attachments-list
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/attachments",
        )
        return self._decode(raw_response, Attachment, plural=True)

    async def download_attachment(
        self,
        issue_id: str,
        attachment_id: str | int,
        filename: str,
    ) -> bytes:
        """
        Use this method to download files attached to issues.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-attachment
        """
        return await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/attachments/{attachment_id}/{filename}",
        )

    async def download_thumbnail(
        self,
        issue_id: str,
        attachment_id: str | int,
    ) -> bytes:
        """
        Get thumbnails of image files attached to issues.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/get-attachment-preview
        """
        return await self._client.request(
            method="GET",
            uri=f"/issues/{issue_id}/thumbnails/{attachment_id}",
        )

    async def attach_file(
        self,
        issue_id: str,
        file: BinaryIO,
        filename: str | None = None,
    ) -> Attachment:
        """
        Attach a file to an issue.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/post-attachment
        """
        form = FormData(fields={"file_data": file})
        raw_response = await self._client.request(
            method="POST",
            uri=f"/issues/{issue_id}/attachments",
            params={"filename": filename} if filename else None,
            form=form,
        )
        return self._decode(raw_response, Attachment)

    async def upload_temp_file(
        self,
        file: BinaryIO,
        filename: str | None = None,
    ) -> Attachment:
        """
        Upload temporary file.

        Use this method to upload a file to Tracker first, and then
        attach it when creating an issue or adding a comment.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/temp-attachment
        """
        form = FormData()
        form.add_field("file_data", file)
        raw_response = await self._client.request(
            method="POST",
            uri="/attachments/",
            params={"filename": filename} if filename else None,
            form=form,
        )
        return self._decode(raw_response, Attachment)

    async def delete_attachment(self, issue_id: str, attachment_id: str | int) -> None:
        """
        Delete attached file.

        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/issues/delete-attachment
        """
        await self._client.request(
            method="DELETE",
            uri=f"/issues/{issue_id}/attachments/{attachment_id}/",
        )
