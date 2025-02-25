from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
import vcr

from ya_tracker_client.domain.client.errors import ClientObjectNotFoundError
from ya_tracker_client.domain.entities.issue import Issue
from ya_tracker_client.domain.entities.issue_status import IssueStatus
from ya_tracker_client.domain.entities.issue_type import IssueType
from ya_tracker_client.domain.entities.priority import Priority
from ya_tracker_client.domain.entities.queue import QueueShort
from ya_tracker_client.domain.entities.user import UserShort


class TestGetIssue:
    @vcr.use_cassette(
        'tests/integration/vcr_cassettes/get_issue_ok.yaml',
        filter_headers=['Authorization', 'X-Cloud-Org-Id'],
        match_on=['uri', 'method'],
    )
    async def test_get_issue__when_issue_found__then_return_it(self, client) -> None:
        # when
        issue = await client.get_issue('TEST-1')
        # then
        assert issue == Issue(
            url='https://api.tracker.yandex.net/v2/issues/TEST-1',
            id='678b278f6eaab8681c533f79',
            key='TEST-1',
            version=1,
            summary='Test',
            favorite=False,
            votes=0,
            type=IssueType(
                url='https://api.tracker.yandex.net/v2/issuetypes/2',
                id='2',
                key='task',
                display='Задача',
            ),
            priority=Priority(
                url='https://api.tracker.yandex.net/v2/priorities/3',
                id=3,
                key='normal',
                display='Средний',
            ),
            queue=QueueShort(
                url='https://api.tracker.yandex.net/v2/queues/TEST',
                id='2',
                key='TEST',
                display='Test',
            ),
            created_at=datetime(2025, 1, 18, 4, 1, 19, 687000, tzinfo=ZoneInfo('UTC')),
            created_by=UserShort(
                url='https://api.tracker.yandex.net/v2/users/8000000000000004',
                id='8000000000000004',
                display='Dmitry Anfimov',
            ),
            updated_by=UserShort(
                url='https://api.tracker.yandex.net/v2/users/8000000000000004',
                id='8000000000000004',
                display='Dmitry Anfimov',
            ),
            updated_at=datetime(2025, 1, 18, 4, 1, 19, 687000, tzinfo=ZoneInfo('UTC')),
            status=IssueStatus(
                url='https://api.tracker.yandex.net/v2/statuses/1',
                id='1',
                key='open',
                display='Открыт',
            ),
        )

    @vcr.use_cassette(
        'tests/integration/vcr_cassettes/get_issue_not_found.yaml',
        filter_headers=['Authorization', 'X-Cloud-Org-Id'],
        match_on=['uri', 'method'],
    )
    async def test_get_issue__when_issue_not_found__then_return_error(self, client) -> None:
        with pytest.raises(ClientObjectNotFoundError):
            await client.get_issue('TEST-100')
