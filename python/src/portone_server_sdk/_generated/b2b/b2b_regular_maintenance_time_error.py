from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bRegularMaintenanceTimeError:
    """금융기관 시스템이 정기 점검 중인 경우
    """
    type: Literal["B2B_REGULAR_MAINTENANCE_TIME"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_regular_maintenance_time_error(obj: B2bRegularMaintenanceTimeError) -> Any:
    entity = {}
    entity["type"] = "B2B_REGULAR_MAINTENANCE_TIME"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_regular_maintenance_time_error(obj: Any) -> B2bRegularMaintenanceTimeError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_REGULAR_MAINTENANCE_TIME":
        raise ValueError(f"{repr(type)} is not 'B2B_REGULAR_MAINTENANCE_TIME'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bRegularMaintenanceTimeError(type, message)
