from http import HTTPStatus
from random import randint
from typing import Any

import pytest

from ya_tacker_client.domain.client import BaseClient
from ya_tacker_client.domain.client.errors import ClientInitTokenError


class ClientForTestInitialization(BaseClient):
    auth_token_header_value = ""
    organisation_token_name = ""

    async def _make_request(
       self,
       method: str,
       url: str,
       params: dict[str, Any] | None = None,
       data: bytes | None = None,
    ) -> tuple[int, bytes]:
        return HTTPStatus.OK, b"Test response body"

    async def stop(self) -> None:
        pass

    def test_authorization_header(self) -> None:
        assert self._headers.get("Authorization") == self.auth_token_header_value

    def test_organisation_header(self) -> None:
        assert self._headers.get(self.organisation_token_name)


def get_client_for_test_initialization(
    organisation_id: str | int,
    oauth_token: str | None = None,
    iam_token: str | None = None,
    auth_token_header_value: str = "",
    organisation_token_name: str = "",
) -> ClientForTestInitialization:
    client = ClientForTestInitialization(
        organisation_id=organisation_id,
        oauth_token=oauth_token,
        iam_token=iam_token,
    )
    client.auth_token_header_value = auth_token_header_value
    client.organisation_token_name = organisation_token_name
    return client


@pytest.mark.parametrize(
    "organisation_id, header_name",
    (
        (randint(1, 1000), "X-Org-Id"),
        (str(randint(1, 1000)), "X-Org-Id"),
        ("test_organisation_id", "X-Cloud-Org-Id"),
    ),
)
def test_init__when_organisation_id_passed__then_use_specific_header_name(organisation_id, header_name) -> None:
    client = get_client_for_test_initialization(
        organisation_id=organisation_id,
        oauth_token="some_token",
        auth_token_header_value="OAuth some_token",
        organisation_token_name=header_name,
    )
    client.test_organisation_header()


def test_init__when_auth_token_not_passed__then_raise_error() -> None:
    with pytest.raises(ClientInitTokenError):
        get_client_for_test_initialization(
            organisation_id=randint(1, 1000),
        )


def test_init__when_oauth_token_passed__then_construct_specific_header_value() -> None:
    client = get_client_for_test_initialization(
        organisation_id=randint(1, 1000),
        oauth_token="some_test_token",
        auth_token_header_value="OAuth some_test_token",
    )
    client.test_authorization_header()


def test_init__when_iam_token_passed__then_construct_specific_header_value() -> None:
    client = get_client_for_test_initialization(
        organisation_id=randint(1, 1000),
        iam_token="some_test_token",
        auth_token_header_value="Bearer some_test_token",
    )
    client.test_authorization_header()
