from __future__ import annotations
from typing import Any, Literal, Optional, Union

Gender = Union[Literal["MALE", "FEMALE", "OTHER"], str]
"""성별
"""


def _serialize_gender(obj: Gender) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_gender(obj: Any) -> Gender:
    return obj
