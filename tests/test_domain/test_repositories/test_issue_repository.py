from random import randint
from typing import Any

import pytest

from tests.fixtures.issue import IssueFactory
from ya_tracker_client.domain.client import BaseClient
from ya_tracker_client.domain.client.errors import ClientObjectNotFoundError
from ya_tracker_client.domain.repositories.issue import IssueRepository


class ClientForIssueRepository(BaseClient):
    make_request_status_code = 200
    make_request_response_body = b"Test response body"

    async def _make_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        data: bytes | None = None,
    ) -> tuple[int, bytes]:
        return self.make_request_status_code, self.make_request_response_body

    async def stop(self) -> None:
        pass


class TestIssueRepository:
    async def test_get_issue__when_issue_not_found__then_raise_error(self) -> None:
        client = ClientForIssueRepository(organisation_id=randint(1, 1000), oauth_token="test_token")
        client.make_request_status_code = 404
        client.make_request_response_body = b""

        with pytest.raises(ClientObjectNotFoundError):
            await IssueRepository(client=client).get_issue("NOT_EXISTS_ISSUE")

    async def test_get_issue__when_issue_found__then_return_it(self, issue_factory: IssueFactory) -> None:
        issue_instance = issue_factory.build()
        client = ClientForIssueRepository(organisation_id=randint(1, 1000), oauth_token="test_token")
        client.make_request_status_code = 200
        client.make_request_response_body = bytes(issue_instance.model_dump_json(), encoding="utf-8")
        assert issue_instance == await IssueRepository(client=client).get_issue("EXISTING_ISSUE")
