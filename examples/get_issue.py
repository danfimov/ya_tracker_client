import os
from asyncio import run

from dotenv import load_dotenv

from ya_tracker_client import YaTrackerClient


load_dotenv()
# from registered application at Yandex OAuth - https://oauth.yandex.ru/
API_TOKEN = os.getenv('API_TOKEN', default=None)
# from admin panel at Yandex Tracker - https://tracker.yandex.ru/admin/orgs
API_ORGANISATION_ID = os.getenv('API_ORGANISATION_ID')

API_HOST = os.getenv('API_HOST', default='https://api.tracker.yandex.net')


async def main() -> None:
    client = YaTrackerClient(
        organisation_id=API_ORGANISATION_ID,
        oauth_token=API_TOKEN,
        api_host=API_HOST,
    )

    await client.get_issue('XYZ-76')

    await client.stop()


if __name__ == '__main__':
    run(main())
