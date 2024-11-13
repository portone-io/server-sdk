from __future__ import annotations
from typing import Any, Literal, Optional, Union

PortOneVersion = Union[Literal["V1", "V2"], str]
"""포트원 버전
"""


def _serialize_port_one_version(obj: PortOneVersion) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_port_one_version(obj: Any) -> PortOneVersion:
    return obj
