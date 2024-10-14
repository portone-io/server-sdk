from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class RemainedAmountLessThanPromotionMinPaymentAmountError:
    """부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
    """
    type: Literal["REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT"] = field(repr=False)
    message: Optional[str]


def _serialize_remained_amount_less_than_promotion_min_payment_amount_error(obj: RemainedAmountLessThanPromotionMinPaymentAmountError) -> Any:
    entity = {}
    entity["type"] = "REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_remained_amount_less_than_promotion_min_payment_amount_error(obj: Any) -> RemainedAmountLessThanPromotionMinPaymentAmountError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT":
        raise ValueError(f"{repr(type)} is not 'REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return RemainedAmountLessThanPromotionMinPaymentAmountError(type, message)
