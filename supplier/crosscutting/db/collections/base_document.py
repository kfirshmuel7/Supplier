from abc import ABC
from typing import Optional


class BaseDocument(ABC):
    __collection__: Optional[str] = None

    _id: str = '_id'
    id: str = '_id'
