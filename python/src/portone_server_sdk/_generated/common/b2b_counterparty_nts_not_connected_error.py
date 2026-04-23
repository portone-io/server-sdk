from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyNtsNotConnectedError:
    """국세청에 연동되어 있지 않은 경우
    """
    message: Optional[str] = field(default=None)
    brn: Optional[str] = field(default=None)
    counterparty_id: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_nts_not_connected_error(obj: B2bCounterpartyNtsNotConnectedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_NTS_NOT_CONNECTED"
    if obj.message is not None:
        entity["message"] = obj.message
    if obj.brn is not None:
        entity["brn"] = obj.brn
    if obj.counterparty_id is not None:
        entity["counterpartyId"] = obj.counterparty_id
    return entity


def _deserialize_b2b_counterparty_nts_not_connected_error(obj: Any) -> B2bCounterpartyNtsNotConnectedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_NTS_NOT_CONNECTED":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_NTS_NOT_CONNECTED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    if "brn" in obj:
        brn = obj["brn"]
        if not isinstance(brn, str):
            raise ValueError(f"{repr(brn)} is not str")
    else:
        brn = None
    if "counterpartyId" in obj:
        counterparty_id = obj["counterpartyId"]
        if not isinstance(counterparty_id, str):
            raise ValueError(f"{repr(counterparty_id)} is not str")
    else:
        counterparty_id = None
    return B2bCounterpartyNtsNotConnectedError(message, brn, counterparty_id)
