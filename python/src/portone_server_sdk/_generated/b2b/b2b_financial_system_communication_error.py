from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bFinancialSystemCommunicationError:
    """금융기관과의 통신에 실패한 경우
    """
    type: Literal["B2B_FINANCIAL_SYSTEM_COMMUNICATION"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_financial_system_communication_error(obj: B2bFinancialSystemCommunicationError) -> Any:
    entity = {}
    entity["type"] = "B2B_FINANCIAL_SYSTEM_COMMUNICATION"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_financial_system_communication_error(obj: Any) -> B2bFinancialSystemCommunicationError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
        raise ValueError(f"{repr(type)} is not 'B2B_FINANCIAL_SYSTEM_COMMUNICATION'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bFinancialSystemCommunicationError(type, message)
