from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyNotFoundError:
    """거래처가 존재하지 않는 경우
    """
    message: Optional[str] = field(default=None)
    counterparty_id: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_not_found_error(obj: B2bCounterpartyNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    if obj.counterparty_id is not None:
        entity["counterpartyId"] = obj.counterparty_id
    return entity


def _deserialize_b2b_counterparty_not_found_error(obj: Any) -> B2bCounterpartyNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_NOT_FOUND":
        raise ValueError("Expected 'B2B_COUNTERPARTY_NOT_FOUND' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    if "counterpartyId" in obj:
        counterparty_id = obj["counterpartyId"]
        if not isinstance(counterparty_id, str):
            raise ValueError("Expected str for counterparty_id")
    else:
        counterparty_id = None
    return B2bCounterpartyNotFoundError(message, counterparty_id)
