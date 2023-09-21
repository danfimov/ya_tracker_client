import os
from asyncio import run

from dotenv import load_dotenv

from ya_tracker_client import YaTrackerClient


load_dotenv()
# from registered application at Yandex OAuth - https://oauth.yandex.ru/
API_TOKEN = os.getenv("API_TOKEN")
# from admin panel at Yandex Tracker - https://tracker.yandex.ru/admin/orgs
API_ORGANISATION_ID = os.getenv("API_ORGANISATION_ID")


async def main() -> None:
    client = YaTrackerClient(
        organisation_id=API_ORGANISATION_ID,
        oauth_token=API_TOKEN,
    )

    me = await client.get_myself()
    print(me)

    me = await client.get_user(me.login, me.uid)
    print(me)

    all_me = await client.get_users()
    print(all_me)

    await client.stop()


if __name__ == "__main__":
    run(main())
