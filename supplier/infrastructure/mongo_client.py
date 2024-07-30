from __future__ import annotations

import dataclasses
from typing import Type, Optional

from pymongo.collection import Collection

from supplier import supplier_settings
from supplier.crosscutting import db
from supplier.infrastructure.mongo_db import MongoDB


@dataclasses.dataclass
class DBConnections:
    mongo_db: Optional[MongoDB] = None


_DB_CONNECTIONS = DBConnections()


def _create_connection(mongo_uri_env_var: str | None = None) -> MongoDB:
    mongo_uri = supplier_settings.get_from_env(mongo_uri_env_var)
    return MongoDB(mongo_uri=mongo_uri)


def _get_mongo_db() -> MongoDB:
    if not _DB_CONNECTIONS.mongo_db:
        _DB_CONNECTIONS.mongo_db = _create_connection()
    _DB_CONNECTIONS.mongo_db.get_or_create_connection()
    return _DB_CONNECTIONS.mongo_db


def get_mongo(collection: Type[db.BaseDocument], ) -> Collection:
    mongo_db = _get_mongo_db()
    collection_name = collection.__collection__ if type(collection) is not str else collection
    return mongo_db.get_collection(collection_name)
