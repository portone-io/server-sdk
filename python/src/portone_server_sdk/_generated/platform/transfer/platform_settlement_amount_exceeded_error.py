from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementAmountExceededError:
    """정산 가능한 금액을 초과한 경우
    """
    requested_amount: int
    """요청 받은 금액
    (int64)
    """
    allowed_amount: int
    """초과한 금액
    (int64)
    """
    message: Optional[str] = field(default=None)
    product_id: Optional[str] = field(default=None)
    """상품 아이디

    주문 항목의 상품 아이디입니다.
    """


def _serialize_platform_settlement_amount_exceeded_error(obj: PlatformSettlementAmountExceededError) -> Any:
    if isinstance(obj, dict):
        return obj
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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED":
        raise ValueError("Expected 'PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED' for type")
    if "requestedAmount" not in obj:
        raise KeyError("Missing required field 'requestedAmount'")
    requested_amount = obj["requestedAmount"]
    if not isinstance(requested_amount, int):
        raise ValueError("Expected int for requested_amount")
    if "allowedAmount" not in obj:
        raise KeyError("Missing required field 'allowedAmount'")
    allowed_amount = obj["allowedAmount"]
    if not isinstance(allowed_amount, int):
        raise ValueError("Expected int for allowed_amount")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    if "productId" in obj:
        product_id = obj["productId"]
        if not isinstance(product_id, str):
            raise ValueError("Expected str for product_id")
    else:
        product_id = None
    return PlatformSettlementAmountExceededError(requested_amount, allowed_amount, message, product_id)
