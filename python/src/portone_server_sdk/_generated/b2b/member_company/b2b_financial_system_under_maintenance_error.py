from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bFinancialSystemUnderMaintenanceError:
    """금융기관 시스템이 점검 중인 경우
    """
    type: Literal["B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_financial_system_under_maintenance_error(obj: B2bFinancialSystemUnderMaintenanceError) -> Any:
    entity = {}
    entity["type"] = "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_financial_system_under_maintenance_error(obj: Any) -> B2bFinancialSystemUnderMaintenanceError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
        raise ValueError(f"{repr(type)} is not 'B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bFinancialSystemUnderMaintenanceError(type, message)
