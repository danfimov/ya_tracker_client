from logging import getLogger
from ssl import create_default_context
from typing import Any

from aiohttp import BytesPayload, ClientSession, ClientTimeout, TCPConnector
from certifi import where

from ya_tracker_client.domain.client import BaseClient


logger = getLogger(__name__)


class AiohttpClient(BaseClient):
    def __init__(
        self,
        organisation_id: str,
        oauth_token: str | None = None,
        iam_token: str | None = None,
        api_host: str = "https://api.tracker.yandex.net",
        api_version: str = "v2",
        timeout: float = 0.,
    ) -> None:
        super().__init__(
            organisation_id,
            oauth_token,
            iam_token,
            api_host,
            api_version,
        )
        self._timeout: ClientTimeout = ClientTimeout(total=timeout)
        self._session: ClientSession | None = None

    def _get_session(self) -> ClientSession:
        """Get cached session. One session per instance."""
        if isinstance(self._session, ClientSession) and not self._session.closed:
            return self._session

        ssl_context = create_default_context(cafile=where())
        connector = TCPConnector(ssl=ssl_context)

        self._session = ClientSession(
            connector=connector,
            headers=self._headers,
            timeout=self._timeout,
        )
        return self._session

    async def _make_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        data: bytes | BytesPayload | None = None,
    ) -> tuple[int, bytes]:
        session = self._get_session()
        async with session.request(method, url, params=params, data=data) as response:
            status = response.status
            body = await response.read()
        self._check_status(status, body)
        return status, body

    async def _stop_session(self) -> None:
        if not isinstance(self._session, ClientSession) or self._session.closed:
            return
        await self._session.close()

    async def stop(self) -> None:
        await self._stop_session()
