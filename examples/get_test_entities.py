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


    try:
        # requests for tests
        me = await client.get_myself()
        await client.get_user(uid=me.uid)
        await client.get_users()
        await client.get_issue('TRACKER-1')
        await client.get_issue('TRACKER-1', expand='transitions')
        await client.get_issue('TRACKER-1', expand='attachments')
        await client.get_issue_transitions('TRACKER-1')
        await client.get_queue('TRACKER')
        await client.get_queue_fields('TRACKER')
        await client.get_queue_versions('TRACKER')
        await client.get_issue_relationships('TRACKER-1')
        await client.get_checklist_items("TRACKER-1")
        await client.get_components()
        await client.get_worklog("TRACKER-1")
        await client.get_worklog_records_by_parameters(me.login)
        await client.get_attachments_list('TRACKER-1')
        await client.get_issue_comments('TRACKER-1')
        await client.get_projects_list(expand='queues')
        await client.get_external_applications()
        await client.get_external_links("TRACKER-1")
        await client.get_macros('TRACKER')
        await client.find_number_of_issues(issue_filter={'queue': 'TRACKER', "assignee": "empty()"})
        await client.get_history_issue_changes('TRACKER-1')
        await client.find_issues()
        await client.get_autoactions('TRACKER')
        await client.get_triggers('TRACKER')
    except Exception as e:
        print('Test failed')
        print(e)
    else:
        print('Test passed')

    await client.stop()


if __name__ == "__main__":
    run(main())
