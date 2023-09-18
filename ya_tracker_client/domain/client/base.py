from abc import ABC, abstractmethod
from http import HTTPStatus
from json import dumps
from logging import getLogger
from typing import Any

from aiohttp import BytesPayload

from ya_tracker_client.domain.client.errors import (
    ClientAuthError,
    ClientError,
    ClientInitTokenError,
    ClientObjectConflictError,
    ClientObjectNotFoundError,
    ClientSufficientRightsError,
)


logger = getLogger(__name__)


class BaseClient(ABC):
    """
    Represents abstract base class for tracker client.
    """

    def __init__(
        self,
        organisation_id: str | int,
        oauth_token: str | None = None,
        iam_token: str | None = None,
        api_host: str = "https://api.tracker.yandex.net",
        api_version: str = "v2",
    ) -> None:
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
    ) -> bytes:
        uri = f"{self._base_url}/{self._api_version}{uri}"

        bytes_payload = BytesPayload(
            value=bytes(dumps(payload), encoding="utf-8"),
            content_type="application/json",
        )

        status, body = await self._make_request(
            method=method,
            url=uri,
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
        data: bytes | BytesPayload | None = None,
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
