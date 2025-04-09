from polyfactory import pytest_plugin

from tests.fixtures.issue import IssueFactory


pytest_plugin.register_fixture(factory=IssueFactory, name='issue_factory')
