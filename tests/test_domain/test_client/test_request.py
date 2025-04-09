from http import HTTPStatus
from logging import getLogger
from random import randint
from typing import Any

import pytest

from ya_tracker_client.domain.client import BaseClient
from ya_tracker_client.domain.client.errors import (
    ClientAuthError,
    ClientError,
    ClientObjectConflictError,
    ClientObjectNotFoundError,
    ClientSufficientRightsError,
)


logger = getLogger(__name__)


class ClientForTestRequestStatus(BaseClient):
    make_request_status_code = 200

    async def _make_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        data: bytes | None = None,
    ) -> tuple[int, bytes]:
        return self.make_request_status_code, b'Test response body'

    async def stop(self) -> None:
        pass


def create_client_for_test_request_status(status_code: int) -> ClientForTestRequestStatus:
    client = ClientForTestRequestStatus(
        organisation_id=randint(1, 1000),
        oauth_token='test_token',
    )
    client.make_request_status_code = status_code
    return client


class TestCheckStatus:
    """Test with all statuses from documentation: https://cloud.yandex.com/en/docs/tracker/error-codes."""

    @pytest.mark.parametrize(
        'status_code',
        [
            HTTPStatus.OK,
            HTTPStatus.CREATED,
            HTTPStatus.NO_CONTENT,
        ],
    )
    async def test_request__when_status_ok__then_not_raise_error(self, status_code: int) -> None:
        client = create_client_for_test_request_status(status_code)
        response_body = await client.request('GET', '/test_uri')
        assert response_body == b'Test response body'

    @pytest.mark.parametrize(
        ('status_code', 'error_type'),
        [
            (HTTPStatus.BAD_REQUEST, ClientError),
            (HTTPStatus.UNAUTHORIZED, ClientAuthError),
            (HTTPStatus.FORBIDDEN, ClientSufficientRightsError),
            (HTTPStatus.NOT_FOUND, ClientObjectNotFoundError),
            (HTTPStatus.CONFLICT, ClientObjectConflictError),
            (HTTPStatus.PRECONDITION_FAILED, ClientObjectConflictError),
            (HTTPStatus.UNPROCESSABLE_ENTITY, ClientError),
            (HTTPStatus.PRECONDITION_REQUIRED, ClientError),
        ],
    )
    async def test_request__when_status_not_ok__then_raise_specific_error(
        self,
        status_code: int,
        error_type: type[ClientError],
    ) -> None:
        client = create_client_for_test_request_status(status_code)
        if error_type == ClientError:  # always raise ClientException with context
            with pytest.raises(error_type, match='Test response body'):
                await client.request('GET', '/test_uri')
        else:
            with pytest.raises(error_type):
                await client.request('GET', '/test_uri')
