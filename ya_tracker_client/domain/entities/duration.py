from re import compile
from typing import Any

from pydantic import model_validator

from ya_tracker_client.domain.entities.base import AbstractEntity


PATTERN = compile(
    r"^P(?=\d+[YMWD])"
    r"((?P<years>\d+)Y)?"
    r"((?P<months>\d+)M)?"
    r"((?P<weeks>\d+)W)?"
    r"((?P<days>\d+)D)?"
    r"(?P<time>T(?=\d+[HMS])"
    r"((?P<hours>\d+)H)?"
    r"((?P<minutes>\d+)M)?"
    r"((?P<seconds>\d+)S)?)?$",
)


class Duration(AbstractEntity):
    years: int = 0
    months: int = 0
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0

    @model_validator(mode="before")
    @classmethod
    def validate(cls, model_value: Any) -> dict | None:
        if not isinstance(model_value, str):
            return

        result = PATTERN.match(model_value)
        if result is None:
            msg = "Duration is not matched to ISO duration pattern."
            raise ValueError(msg)

        data: dict[str, int] = {}
        for field in Duration.model_fields:
            if value := result.group(field):
                data[field] = int(value)
        return data

    def __str__(self) -> str:
        time = ""
        if self.hours:
            time = f"{time}{self.hours}H"
        if self.minutes:
            time = f"{time}{self.minutes}M"
        if self.seconds:
            time = f"{time}{self.seconds}S"

        duration = "P"
        if self.years:
            duration = f"{duration}{self.years}Y"
        if self.months:
            duration = f"{duration}{self.months}M"
        if self.days:
            duration = f"{duration}{self.days}D"
        if time:
            duration = f"{duration}T{time}"

        return duration

