from polyfactory.factories import pydantic_factory

from ya_tracker_client.domain.entities.issue import Issue


class IssueFactory(pydantic_factory.ModelFactory[Issue]):
    pass
