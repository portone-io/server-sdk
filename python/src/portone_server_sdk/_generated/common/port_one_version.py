from __future__ import annotations
from typing import Any, Literal, Optional

PortOneVersion = Literal["V1", "V2"]
"""포트원 버전
"""


def _serialize_port_one_version(obj: PortOneVersion) -> Any:
    return obj


def _deserialize_port_one_version(obj: Any) -> PortOneVersion:
    if obj not in ["V1", "V2"]:
        raise ValueError(f"{repr(obj)} is not PortOneVersion")
    return obj
