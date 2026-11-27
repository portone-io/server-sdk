from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.create_platform_order_transfer_body_additional_fee import CreatePlatformOrderTransferBodyAdditionalFee, _deserialize_create_platform_order_transfer_body_additional_fee, _serialize_create_platform_order_transfer_body_additional_fee
from ...platform.transfer.create_platform_order_transfer_body_discount import CreatePlatformOrderTransferBodyDiscount, _deserialize_create_platform_order_transfer_body_discount, _serialize_create_platform_order_transfer_body_discount
from ...platform.transfer.create_platform_order_transfer_body_product import CreatePlatformOrderTransferBodyProduct, _deserialize_create_platform_order_transfer_body_product, _serialize_create_platform_order_transfer_body_product

@dataclass
class CreatePlatformOrderTransferBodyOrderLine:
    """주문 항목
    """
    product: CreatePlatformOrderTransferBodyProduct
    """상품
    """
    quantity: int
    """상품 수량
    (int32)
    """
    discounts: list[CreatePlatformOrderTransferBodyDiscount]
    """상품 할인 정보
    """
    additional_fees: list[CreatePlatformOrderTransferBodyAdditionalFee]
    """상품 추가 수수료 정보
    """


def _serialize_create_platform_order_transfer_body_order_line(obj: CreatePlatformOrderTransferBodyOrderLine) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["product"] = _serialize_create_platform_order_transfer_body_product(obj.product)
    entity["quantity"] = obj.quantity
    entity["discounts"] = list(map(_serialize_create_platform_order_transfer_body_discount, obj.discounts))
    entity["additionalFees"] = list(map(_serialize_create_platform_order_transfer_body_additional_fee, obj.additional_fees))
    return entity


def _deserialize_create_platform_order_transfer_body_order_line(obj: Any) -> CreatePlatformOrderTransferBodyOrderLine:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "product" not in obj:
        raise KeyError("Missing required field 'product'")
    product = obj["product"]
    product = _deserialize_create_platform_order_transfer_body_product(product)
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
        item = _deserialize_create_platform_order_transfer_body_discount(item)
        discounts[i] = item
    if "additionalFees" not in obj:
        raise KeyError("Missing required field 'additionalFees'")
    additional_fees = obj["additionalFees"]
    if not isinstance(additional_fees, list):
        raise ValueError("Expected list for additional_fees")
    for i, item in enumerate(additional_fees):
        item = _deserialize_create_platform_order_transfer_body_additional_fee(item)
        additional_fees[i] = item
    return CreatePlatformOrderTransferBodyOrderLine(product, quantity, discounts, additional_fees)
