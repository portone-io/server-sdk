from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementParameterNotFoundError:
    """정산 파라미터가 존재하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_settlement_parameter_not_found_error(obj: PlatformSettlementParameterNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_settlement_parameter_not_found_error(obj: Any) -> PlatformSettlementParameterNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND":
        raise ValueError("Expected 'PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformSettlementParameterNotFoundError(message)
