from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_additional_fee import CreatePlatformOrderTransferBodyAdditionalFee, _deserialize_create_platform_order_transfer_body_additional_fee, _serialize_create_platform_order_transfer_body_additional_fee
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_discount import CreatePlatformOrderTransferBodyDiscount, _deserialize_create_platform_order_transfer_body_discount, _serialize_create_platform_order_transfer_body_discount
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_product import CreatePlatformOrderTransferBodyProduct, _deserialize_create_platform_order_transfer_body_product, _serialize_create_platform_order_transfer_body_product

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
    entity = {}
    entity["product"] = _serialize_create_platform_order_transfer_body_product(obj.product)
    entity["quantity"] = obj.quantity
    entity["discounts"] = list(map(_serialize_create_platform_order_transfer_body_discount, obj.discounts))
    entity["additionalFees"] = list(map(_serialize_create_platform_order_transfer_body_additional_fee, obj.additional_fees))
    return entity


def _deserialize_create_platform_order_transfer_body_order_line(obj: Any) -> CreatePlatformOrderTransferBodyOrderLine:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "product" not in obj:
        raise KeyError(f"'product' is not in {obj}")
    product = obj["product"]
    product = _deserialize_create_platform_order_transfer_body_product(product)
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
        item = _deserialize_create_platform_order_transfer_body_discount(item)
        discounts[i] = item
    if "additionalFees" not in obj:
        raise KeyError(f"'additionalFees' is not in {obj}")
    additional_fees = obj["additionalFees"]
    if not isinstance(additional_fees, list):
        raise ValueError(f"{repr(additional_fees)} is not list")
    for i, item in enumerate(additional_fees):
        item = _deserialize_create_platform_order_transfer_body_additional_fee(item)
        additional_fees[i] = item
    return CreatePlatformOrderTransferBodyOrderLine(product, quantity, discounts, additional_fees)
