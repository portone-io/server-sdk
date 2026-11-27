from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCounterpartyNotConnectedError:
    """파트너가 거래처로 연동 되어있지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_counterparty_not_connected_error(obj: PlatformCounterpartyNotConnectedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_COUNTERPARTY_NOT_CONNECTED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_counterparty_not_connected_error(obj: Any) -> PlatformCounterpartyNotConnectedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_COUNTERPARTY_NOT_CONNECTED":
        raise ValueError("Expected 'PLATFORM_COUNTERPARTY_NOT_CONNECTED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformCounterpartyNotConnectedError(message)
