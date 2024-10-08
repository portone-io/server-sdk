from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.create_platform_order_cancel_transfer_body_discount import CreatePlatformOrderCancelTransferBodyDiscount, _deserialize_create_platform_order_cancel_transfer_body_discount, _serialize_create_platform_order_cancel_transfer_body_discount

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
    entity = {}
    entity["productId"] = obj.product_id
    entity["quantity"] = obj.quantity
    entity["discounts"] = list(map(_serialize_create_platform_order_cancel_transfer_body_discount, obj.discounts))
    return entity


def _deserialize_create_platform_order_cancel_transfer_body_order_line(obj: Any) -> CreatePlatformOrderCancelTransferBodyOrderLine:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "productId" not in obj:
        raise KeyError(f"'productId' is not in {obj}")
    product_id = obj["productId"]
    if not isinstance(product_id, str):
        raise ValueError(f"{repr(product_id)} is not str")
    if "quantity" not in obj:
        raise KeyError(f"'quantity' is not in {obj}")
    quantity = obj["quantity"]
    if not isinstance(quantity, int):
        raise ValueError(f"{repr(quantity)} is not int")
    if "discounts" not in obj:
        raise KeyError(f"'discounts' is not in {obj}")
    discounts = obj["discounts"]
    if not isinstance(discounts, list):
        raise ValueError(f"{repr(discounts)} is not list")
    for i, item in enumerate(discounts):
        item = _deserialize_create_platform_order_cancel_transfer_body_discount(item)
        discounts[i] = item
    return CreatePlatformOrderCancelTransferBodyOrderLine(product_id, quantity, discounts)
