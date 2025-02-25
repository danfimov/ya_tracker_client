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
    if not API_ORGANISATION_ID:
        raise RuntimeError('API_ORGANISATION_ID must be set')

    client = YaTrackerClient(
        organisation_id=API_ORGANISATION_ID,
        oauth_token=API_TOKEN,
    )


    try:
        # requests for tests
        me = await client.get_myself()
        await client.get_user(uid=me.uid)
        await client.get_users()
        await client.get_issue('TEST-1')
        await client.get_issue('TEST-1', expand='transitions')
        await client.get_issue('TEST-1', expand='attachments')
        await client.get_issue_transitions('TEST-1')
        await client.get_queue('TEST')
        await client.get_queue_fields('TEST')
        await client.get_queue_versions('TEST')
        await client.get_issue_relationships('TEST-1')
        await client.get_checklist_items("TEST-1")
        await client.get_components()
        await client.get_worklog("TEST-1")
        await client.get_worklog_records_by_parameters(me.login)
        await client.get_attachments_list('TEST-1')
        await client.get_issue_comments('TEST-1')
        await client.get_projects_list(expand='queues')
        await client.get_external_applications()
        await client.get_external_links("TEST-1")
        await client.get_macros('TEST')
        await client.find_number_of_issues(issue_filter={'queue': 'TEST', "assignee": "empty()"})
        await client.get_history_issue_changes('TEST-1')
        await client.find_issues()
        await client.get_autoactions('TEST')
        await client.get_triggers('TEST')
    except Exception as e:
        print('Test failed')
        print(e)
    else:
        print('Test passed')

    await client.stop()


if __name__ == "__main__":
    run(main())
