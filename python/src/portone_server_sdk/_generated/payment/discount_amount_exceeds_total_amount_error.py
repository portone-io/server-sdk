from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DiscountAmountExceedsTotalAmountError:
    """프로모션 할인 금액이 결제 시도 금액 이상인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_discount_amount_exceeds_total_amount_error(obj: DiscountAmountExceedsTotalAmountError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_discount_amount_exceeds_total_amount_error(obj: Any) -> DiscountAmountExceedsTotalAmountError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
        raise ValueError("Expected 'DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return DiscountAmountExceedsTotalAmountError(message)
