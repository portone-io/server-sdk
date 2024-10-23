from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bHometaxUnderMaintenanceError:
    """홈택스가 점검중이거나 순단이 발생한 경우
    """
    type: Literal["B2B_HOMETAX_UNDER_MAINTENANCE"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_hometax_under_maintenance_error(obj: B2bHometaxUnderMaintenanceError) -> Any:
    entity = {}
    entity["type"] = "B2B_HOMETAX_UNDER_MAINTENANCE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_hometax_under_maintenance_error(obj: Any) -> B2bHometaxUnderMaintenanceError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_HOMETAX_UNDER_MAINTENANCE":
        raise ValueError(f"{repr(type)} is not 'B2B_HOMETAX_UNDER_MAINTENANCE'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bHometaxUnderMaintenanceError(type, message)
