from pydantic import Field

from ya_tracker_client.domain.entities.action import Action
from ya_tracker_client.domain.entities.base import AbstractEntity
from ya_tracker_client.domain.entities.queue import QueueShort


class TriggerConditionType(AbstractEntity):
    type: str = Field(
        examples=[
            "CommentNoneMatchCondition",
            "CommentStringNotMatchCondition",
            "CommentFullyMatchCondition",
            "CommentAnyMatchCondition",
            "CommentStringMatchCondition",
            "CommentAuthorNot",
            "CommentAuthor",
            "CommentMessageExternal",
            "CommentMessageInternal",
        ],
    )  # TODO: add validators for strings with examples (or replace it with Enum)


class TriggerCondition(AbstractEntity):
    type: str = Field(examples=["or", "and"])
    conditions: list[TriggerConditionType]


class Trigger(AbstractEntity):
    id: str | int
    url: str
    queue: QueueShort | str
    name: str
    order: str
    actions: list[Action]
    conditions: list[TriggerCondition | TriggerConditionType] = Field(default_factory=list)
    version: int
    active: bool


class TriggerCreate(AbstractEntity):
    name: str
    actions: list[Action]
    conditions: list[TriggerCondition] | None = Field(default_factory=list)
    active: bool | None = None
