from abc import ABCMeta

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


def tracker_alias_generator(s: str) -> str:
    """Convert a string from snake case to camel case and rename url to self"""
    if s == "url":
        return "self"
    return to_camel(s)


class AbstractEntity(BaseModel, metaclass=ABCMeta):
    model_config = ConfigDict(alias_generator=tracker_alias_generator, populate_by_name=True)
