from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class CancellableAmountConsistencyBrokenError:
    """취소 가능 잔액 검증에 실패한 경우
    """
    type: Literal["CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN"] = field(repr=False)
    message: Optional[str]


def _serialize_cancellable_amount_consistency_broken_error(obj: CancellableAmountConsistencyBrokenError) -> Any:
    entity = {}
    entity["type"] = "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_cancellable_amount_consistency_broken_error(obj: Any) -> CancellableAmountConsistencyBrokenError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN":
        raise ValueError(f"{repr(type)} is not 'CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return CancellableAmountConsistencyBrokenError(type, message)
