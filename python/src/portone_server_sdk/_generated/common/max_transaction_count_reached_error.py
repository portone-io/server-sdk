from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class MaxTransactionCountReachedError:
    """결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_max_transaction_count_reached_error(obj: MaxTransactionCountReachedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MAX_TRANSACTION_COUNT_REACHED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_max_transaction_count_reached_error(obj: Any) -> MaxTransactionCountReachedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "MAX_TRANSACTION_COUNT_REACHED":
        raise ValueError(f"{repr(type)} is not 'MAX_TRANSACTION_COUNT_REACHED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return MaxTransactionCountReachedError(message)
