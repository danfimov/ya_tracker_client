from abc import ABC, abstractmethod
from http import HTTPStatus
from logging import getLogger
from typing import Any

from aiohttp import BytesPayload, FormData

from ya_tracker_client.domain.client.errors import (
    ClientAuthError,
    ClientError,
    ClientInitTokenError,
    ClientObjectConflictError,
    ClientObjectNotFoundError,
    ClientSufficientRightsError,
)
from ya_tracker_client.utils import serialize_entity


logger = getLogger(__name__)


class BaseClient(ABC):
    """
    Represents abstract base class for tracker client.
    """

    def __init__(
        self,
        organisation_id: str | int | None = None,
        oauth_token: str | None = None,
        iam_token: str | None = None,
        api_host: str = "https://api.tracker.yandex.net",
        api_version: str = "v2",
    ) -> None:
        """
        :param organisation_id: ID from admin panel at Yandex Tracker. No needed for Yandex developers.
        :param oauth_token: OAuth token from registered application at Yandex OAuth - https://oauth.yandex.ru/
        :param iam_token: IAM token from registered application at Yandex OAuth - https://oauth.yandex.ru/
        :param api_host: Host of your Tracker. For Yandex developers - https://st-api.yandex-team.ru
        :param api_version: Version of API. Currently supported only v2 version.
        """
        self._headers: dict[str, str] = {}

        # Yandex 360 uses integer identifiers and Yandex Cloud prefer strings in identifiers
        if isinstance(organisation_id, int) or organisation_id.isdigit():
            self._headers["X-Org-Id"] = str(organisation_id)
        else:
            self._headers["X-Cloud-Org-Id"] = organisation_id

        if oauth_token is not None:
            self._headers["Authorization"] = f"OAuth {oauth_token}"
        elif iam_token is not None:
            self._headers["Authorization"] = f"Bearer {iam_token}"
        else:
            raise ClientInitTokenError

        self._base_url = api_host
        self._api_version = api_version

    async def request(
        self,
        method: str,
        uri: str,
        params: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
        form: FormData | None = None,
    ) -> bytes:
        if form:
            bytes_payload = form
        else:
            bytes_payload = BytesPayload(
                value=bytes(serialize_entity(payload), encoding="utf-8"),
                content_type="application/json",
            )

        status, body = await self._make_request(
            method=method,
            url=f"{self._base_url}/{self._api_version}{uri}",
            params=params,
            data=bytes_payload,
        )
        self._check_status(status, body)
        return body

    @abstractmethod
    async def _make_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        data: bytes | BytesPayload | FormData | None = None,
    ) -> tuple[int, bytes]:
        """
        Get raw response from via http-client.

        :returns: tuple of (status_code, response_body).
        """

    @staticmethod
    def _check_status(status: int, body: bytes) -> None:
        if status <= HTTPStatus.IM_USED:
            return

        logger.exception("Response error. Status: %s. Body: %s", status, body)

        match status:
            case HTTPStatus.UNAUTHORIZED:
                raise ClientAuthError
            case HTTPStatus.FORBIDDEN:
                raise ClientSufficientRightsError
            case HTTPStatus.NOT_FOUND:
                raise ClientObjectNotFoundError
            case HTTPStatus.CONFLICT:
                raise ClientObjectConflictError
            case HTTPStatus.PRECONDITION_FAILED:
                raise ClientObjectConflictError
            case _:
                raise ClientError(body)

    @abstractmethod
    async def stop(self) -> None:
        """
        Stop client gracefully - close all sessions.
        """
