from __future__ import annotations
from typing import Any, Literal, Optional, Union

Trigger = Union[Literal["CONSOLE", "API", "PORTONE_ADMIN"], str]


def _serialize_trigger(obj: Trigger) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_trigger(obj: Any) -> Trigger:
    return obj
