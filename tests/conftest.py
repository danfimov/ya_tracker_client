import os

import pytest
from dotenv import load_dotenv

from ya_tracker_client import YaTrackerClient


@pytest.fixture
def client() -> YaTrackerClient:
    load_dotenv()
    return YaTrackerClient(
        organisation_id=os.getenv('API_ORGANISATION_ID'),
        oauth_token=os.getenv('API_TOKEN', default=None),
        api_host=os.getenv('API_HOST', default='https://api.tracker.yandex.net'),
    )
