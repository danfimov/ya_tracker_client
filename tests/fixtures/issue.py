from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture

from ya_tracker_client.domain.entities.issue import Issue


@register_fixture
class IssueFactory(ModelFactory[Issue]):
    __model__ = Issue
