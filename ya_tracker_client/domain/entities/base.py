from abc import ABCMeta

from pydantic import BaseModel


class AbstractEntity(BaseModel, metaclass=ABCMeta):
    ...
