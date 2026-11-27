from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerPendingNtsOperationError:
    """파트너의 국세청 연동/해제가 진행 중인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_partner_pending_nts_operation_error(obj: PlatformPartnerPendingNtsOperationError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_PARTNER_PENDING_NTS_OPERATION"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_partner_pending_nts_operation_error(obj: Any) -> PlatformPartnerPendingNtsOperationError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_PARTNER_PENDING_NTS_OPERATION":
        raise ValueError("Expected 'PLATFORM_PARTNER_PENDING_NTS_OPERATION' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformPartnerPendingNtsOperationError(message)
