from __future__ import annotations
from typing import Any, Literal, Optional

Gender = Literal["MALE", "FEMALE", "OTHER"]
"""성별
"""


def _serialize_gender(obj: Gender) -> Any:
    return obj


def _deserialize_gender(obj: Any) -> Gender:
    if obj not in ["MALE", "FEMALE", "OTHER"]:
        raise ValueError(f"{repr(obj)} is not Gender")
    return obj
