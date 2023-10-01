# Yandex Tracker Client (or Yet Another Tracker Client)

Async Yandex Tracker Client based on aiohttp and pydantic

[![Python](https://img.shields.io/badge/python-^3.10-blue)](https://www.python.org/)
[![Code linter: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Linters](https://github.com/danfimov/ya_tracker_client/actions/workflows/code-check.yml/badge.svg)](https://github.com/danfimov/ya_tracker_client/actions/workflows/code-check.yml)

---

API docs: https://cloud.yandex.com/en/docs/tracker/about-api

## Installation

```shell
pip install ya_tracker_client
```

or 

```shell
poetry add ya_tracker_client
```


## Usage

```python
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
    # init client
    client = YaTrackerClient(
        organisation_id=API_ORGANISATION_ID,
        oauth_token=API_TOKEN,
    )
    
    # create issue
    new_issue = await client.create_issue('New issue', 'TRACKER-QUEUE')
    
     # get issue
    issue = await client.get_issue('KEY-1')
    
    # update issue (just pass kwargs)
    issue = await client.edit_issue('KEY-1', description='Hello World')
    
    # don't forget to close tracker on app shutdown
    await client.stop()


if __name__ == "__main__":
    run(main())
```


## Explanations about naming

- All `self` properties renamed to `url` cause it's incompatible with Python;
- All `camelCase` properties renamed to `pythonic_case`;
- All datetime values converted to python's `datetime.datetime` objects;
- Methods named by author, cause Yandex API has no clear method names.

## Current library capabilities

- Working with queues
- Getting information about issues, priorities and transitions
- Working with issue relationships
- Getting user information

More info about work status here: https://github.com/danfimov/ya_tracker_client/milestone/1
