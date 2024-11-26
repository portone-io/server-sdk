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
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
        raise ValueError(f"{repr(type)} is not 'DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return DiscountAmountExceedsTotalAmountError(message)
