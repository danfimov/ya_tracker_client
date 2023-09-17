import os
from asyncio import run

from dotenv import load_dotenv

from ya_tacker_client import YaTrackerClient


load_dotenv()
# from registered application at Yandex OAuth - https://oauth.yandex.ru/
API_TOKEN = os.getenv('API_TOKEN')
# from admin panel at Yandex Tracker - https://tracker.yandex.ru/admin/orgs
API_ORGANISATION_ID = os.getenv('API_ORGANISATION_ID')


async def main() -> None:
    client = YaTrackerClient(
        organisation_id=API_ORGANISATION_ID,
        oauth_token=API_TOKEN,
    )
    issue = await client.get_issue('TRACKER-1')
    print(issue)
    await client.stop()


if __name__ == '__main__':
    run(main())
