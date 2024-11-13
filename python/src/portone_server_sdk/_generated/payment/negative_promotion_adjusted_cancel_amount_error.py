from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class NegativePromotionAdjustedCancelAmountError:
    """프로모션에 의해 조정된 취소 금액이 음수인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_negative_promotion_adjusted_cancel_amount_error(obj: NegativePromotionAdjustedCancelAmountError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "NEGATIVE_PROMOTION_ADJUSTED_CANCEL_AMOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_negative_promotion_adjusted_cancel_amount_error(obj: Any) -> NegativePromotionAdjustedCancelAmountError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "NEGATIVE_PROMOTION_ADJUSTED_CANCEL_AMOUNT":
        raise ValueError(f"{repr(type)} is not 'NEGATIVE_PROMOTION_ADJUSTED_CANCEL_AMOUNT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return NegativePromotionAdjustedCancelAmountError(message)
