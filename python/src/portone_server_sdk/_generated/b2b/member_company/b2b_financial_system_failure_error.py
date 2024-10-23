from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bFinancialSystemFailureError:
    """금융기관 장애
    """
    type: Literal["B2B_FINANCIAL_SYSTEM_FAILURE"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_financial_system_failure_error(obj: B2bFinancialSystemFailureError) -> Any:
    entity = {}
    entity["type"] = "B2B_FINANCIAL_SYSTEM_FAILURE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_financial_system_failure_error(obj: Any) -> B2bFinancialSystemFailureError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_FINANCIAL_SYSTEM_FAILURE":
        raise ValueError(f"{repr(type)} is not 'B2B_FINANCIAL_SYSTEM_FAILURE'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bFinancialSystemFailureError(type, message)
