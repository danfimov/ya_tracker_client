from datetime import datetime
from decimal import Decimal
from json import JSONEncoder, dumps
from uuid import UUID
from zoneinfo import ZoneInfo

from yarl import URL


class UpgradedJSONEncoder(JSONEncoder):
    def default(self, entity):
        if isinstance(entity, datetime):
            if entity.tzinfo is None:  # for YYYY-MM-DDThh:mm:ss.sss±hhmm format
                entity = entity.replace(tzinfo=ZoneInfo("UTC"))
            return entity.isoformat()

        if isinstance(entity, Decimal) or isinstance(entity, UUID):
            return str(entity)

        if isinstance(entity, URL):
            return str(entity)

        return JSONEncoder.default(self, entity)


def serialize_entity(entity):
    return dumps(entity, cls=UpgradedJSONEncoder)


__all__ = [
    "serialize_entity",
]
