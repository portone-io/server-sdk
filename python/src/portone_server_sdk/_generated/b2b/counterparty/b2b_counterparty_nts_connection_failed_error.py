from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyNtsConnectionFailedError:
    """국세청 연동에 실패한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_nts_connection_failed_error(obj: B2bCounterpartyNtsConnectionFailedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_NTS_CONNECTION_FAILED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_nts_connection_failed_error(obj: Any) -> B2bCounterpartyNtsConnectionFailedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_NTS_CONNECTION_FAILED":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_NTS_CONNECTION_FAILED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartyNtsConnectionFailedError(message)
