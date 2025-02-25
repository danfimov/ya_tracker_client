import vcr

from ya_tracker_client.domain.entities.component import Component
from ya_tracker_client.domain.entities.queue import QueueShort
from ya_tracker_client.domain.entities.user import UserShort


class TestGetComponents:
    @vcr.use_cassette(
        'tests/integration/vcr_cassettes/get_standard_components.yaml',
        filter_headers=['Authorization', 'X-Cloud-Org-Id'],
    )
    async def test_get_components__when_standard_components_exists__then_return_them(self, client) -> None:
        # when
        components = await client.get_components()
        # then
        assert components == [
            Component(
                url='https://api.tracker.yandex.net/v2/components/1',
                id=1, version=1, name='Фронтенд',
                queue=QueueShort(
                    url='https://api.tracker.yandex.net/v2/queues/DANFIMOV',
                    id='1',
                    key='DANFIMOV',
                    display='Персональная очередь',
                ),
                description=None,
                lead=None,
                assign_auto=False,
            ),
            Component(
                url='https://api.tracker.yandex.net/v2/components/2',
                id=2, version=1, name='Бекенд',
                queue=QueueShort(
                    url='https://api.tracker.yandex.net/v2/queues/DANFIMOV',
                    id='1',
                    key='DANFIMOV',
                    display='Персональная очередь',
                ),
                description=None,
                lead=None,
                assign_auto=False,
            ),
        ]

    @vcr.use_cassette(
        'tests/integration/vcr_cassettes/get_custom_component.yaml',
        filter_headers=['Authorization', 'X-Cloud-Org-Id'],
    )
    async def test_get_components__when_custom_component_exists__then_return_it(self, client) -> None:
        # when
        components = await client.get_components()
        # then
        assert Component(
            url='https://api.tracker.yandex.net/v2/components/4',
            id=4,
            version=2,
            name='Custom',
            queue=QueueShort(
                url='https://api.tracker.yandex.net/v2/queues/DANFIMOV',
                id='1',
                key='DANFIMOV',
                display='Персональная очередь',
            ),
            description='Описание',
            lead=UserShort(
                url='https://api.tracker.yandex.net/v2/users/8000000000000004',
                id='8000000000000004',
                display='Dmitry Anfimov',
            ),
            assign_auto=True,
        ) == components[2]
