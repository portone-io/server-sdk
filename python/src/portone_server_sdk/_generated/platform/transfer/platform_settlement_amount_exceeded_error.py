from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementAmountExceededError:
    """정산 가능한 금액을 초과한 경우
    """
    type: Literal["PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED"] = field(repr=False)
    requested_amount: int
    """요청 받은 금액
    (int64)
    """
    allowed_amount: int
    """초과한 금액
    (int64)
    """
    message: Optional[str]
    product_id: Optional[str]
    """상품 아이디

    주문 항목의 상품 아이디입니다.
    """


def _serialize_platform_settlement_amount_exceeded_error(obj: PlatformSettlementAmountExceededError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED"
    entity["requestedAmount"] = obj.requested_amount
    entity["allowedAmount"] = obj.allowed_amount
    if obj.message is not None:
        entity["message"] = obj.message
    if obj.product_id is not None:
        entity["productId"] = obj.product_id
    return entity


def _deserialize_platform_settlement_amount_exceeded_error(obj: Any) -> PlatformSettlementAmountExceededError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED'")
    if "requestedAmount" not in obj:
        raise KeyError(f"'requestedAmount' is not in {obj}")
    requested_amount = obj["requestedAmount"]
    if not isinstance(requested_amount, int):
        raise ValueError(f"{repr(requested_amount)} is not int")
    if "allowedAmount" not in obj:
        raise KeyError(f"'allowedAmount' is not in {obj}")
    allowed_amount = obj["allowedAmount"]
    if not isinstance(allowed_amount, int):
        raise ValueError(f"{repr(allowed_amount)} is not int")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    if "productId" in obj:
        product_id = obj["productId"]
        if not isinstance(product_id, str):
            raise ValueError(f"{repr(product_id)} is not str")
    else:
        product_id = None
    return PlatformSettlementAmountExceededError(type, requested_amount, allowed_amount, message, product_id)
