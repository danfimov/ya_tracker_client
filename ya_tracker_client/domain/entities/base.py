from abc import ABCMeta

import pydantic
from pydantic import BaseModel, ConfigDict


if int(pydantic.VERSION[0]) == 2:
    from pydantic.alias_generators import to_camel
else:
    from re import sub


    def to_camel(snake: str) -> str:
        """
        Convert a snake_case string to camelCase.

        :param snake: The string to convert.
        :return: The converted camelCase string.
        """
        camel = snake.title()
        camel = sub("([0-9A-Za-z])_(?=[0-9A-Z])", lambda m: m.group(1), camel)  # to PascalCase first
        return sub("(^_*[A-Z])", lambda m: m.group(1).lower(), camel)


def tracker_alias_generator(s: str) -> str:
    """Convert a string from snake case to camel case and rename url to self"""
    if s == "url":
        return "self"
    return to_camel(s)


class AbstractEntity(BaseModel, metaclass=ABCMeta):
    model_config = ConfigDict(alias_generator=tracker_alias_generator, populate_by_name=True)
