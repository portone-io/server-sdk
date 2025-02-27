from __future__ import annotations
from typing import Any, Literal, Optional, Union

DisputeStatus = Union[Literal["UNRESOLVED", "RESOLVED"], str]
"""분쟁 상태
"""


def _serialize_dispute_status(obj: DisputeStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_dispute_status(obj: Any) -> DisputeStatus:
    return obj
