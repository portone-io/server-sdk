from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.create_platform_order_cancel_transfer_body_discount import CreatePlatformOrderCancelTransferBodyDiscount, _deserialize_create_platform_order_cancel_transfer_body_discount, _serialize_create_platform_order_cancel_transfer_body_discount

@dataclass
class CreatePlatformOrderCancelTransferBodyOrderLine:
    """주문 취소 항목 리스트
    """
    product_id: str
    """상품 아이디
    """
    quantity: int
    """상품 수량
    (int32)
    """
    discounts: list[CreatePlatformOrderCancelTransferBodyDiscount]
    """상품 할인 정보
    """


def _serialize_create_platform_order_cancel_transfer_body_order_line(obj: CreatePlatformOrderCancelTransferBodyOrderLine) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["productId"] = obj.product_id
    entity["quantity"] = obj.quantity
    entity["discounts"] = list(map(_serialize_create_platform_order_cancel_transfer_body_discount, obj.discounts))
    return entity


def _deserialize_create_platform_order_cancel_transfer_body_order_line(obj: Any) -> CreatePlatformOrderCancelTransferBodyOrderLine:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "productId" not in obj:
        raise KeyError("Missing required field 'productId'")
    product_id = obj["productId"]
    if not isinstance(product_id, str):
        raise ValueError("Expected str for product_id")
    if "quantity" not in obj:
        raise KeyError("Missing required field 'quantity'")
    quantity = obj["quantity"]
    if not isinstance(quantity, int):
        raise ValueError("Expected int for quantity")
    if "discounts" not in obj:
        raise KeyError("Missing required field 'discounts'")
    discounts = obj["discounts"]
    if not isinstance(discounts, list):
        raise ValueError("Expected list for discounts")
    for i, item in enumerate(discounts):
        item = _deserialize_create_platform_order_cancel_transfer_body_discount(item)
        discounts[i] = item
    return CreatePlatformOrderCancelTransferBodyOrderLine(product_id, quantity, discounts)
