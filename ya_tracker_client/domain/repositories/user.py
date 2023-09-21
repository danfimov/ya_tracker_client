from json import loads
from logging import getLogger

from ya_tracker_client.domain.client.errors import ClientError
from ya_tracker_client.domain.entities.user import User
from ya_tracker_client.domain.repositories.base import EntityRepository


logger = getLogger(__name__)


class UserRepository(EntityRepository):
    async def get_myself(self) -> User:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/get-user-info
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/myself/",
        )
        return User(**loads(raw_response))

    async def get_user(
        self,
        login: str | None = None,
        uid: int | None = None,
    ) -> User:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/get-user
        """
        if (login is None) and (uid is None):
            raise ClientError("Please provide login or uid for this request")
        elif (login is not None) and (uid is not None):
            logger.warning(
                "Login will be used for this request. Please provide only login or only uid for this request, not both",
            )

        raw_response = await self._client.request(
            method="GET",
            uri=f"/users/{login or uid}",
        )
        return User(**loads(raw_response))

    async def get_users(self) -> list[User]:
        """
        Yandex Cloud documentation for method: https://cloud.yandex.ru/docs/tracker/get-users
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/users/",
        )
        return [User(**raw_user) for raw_user in loads(raw_response)]
