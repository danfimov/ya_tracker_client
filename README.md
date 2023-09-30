# Yandex Tracker Client (or Yet Another Tracker Client)

Async Yandex Tracker Client based on aiohttp and pydantic (v2)

[![Python](https://img.shields.io/badge/python-^3.11-blue)](https://www.python.org/)
[![Code linter: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Linters](https://github.com/danfimov/ya_tracker_client/actions/workflows/code-check.yml/badge.svg)](https://github.com/danfimov/ya_tracker_client/actions/workflows/code-check.yml)

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
