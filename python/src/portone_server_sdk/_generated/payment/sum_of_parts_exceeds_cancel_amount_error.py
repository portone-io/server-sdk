from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class SumOfPartsExceedsCancelAmountError:
    """면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_sum_of_parts_exceeds_cancel_amount_error(obj: SumOfPartsExceedsCancelAmountError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_sum_of_parts_exceeds_cancel_amount_error(obj: Any) -> SumOfPartsExceedsCancelAmountError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT":
        raise ValueError("Expected 'SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return SumOfPartsExceedsCancelAmountError(message)
