from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_order_settlement_amount import PlatformOrderSettlementAmount, _deserialize_platform_order_settlement_amount, _serialize_platform_order_settlement_amount
from ...platform.transfer.platform_order_transfer_additional_fee import PlatformOrderTransferAdditionalFee, _deserialize_platform_order_transfer_additional_fee, _serialize_platform_order_transfer_additional_fee
from ...platform.transfer.platform_order_transfer_discount import PlatformOrderTransferDiscount, _deserialize_platform_order_transfer_discount, _serialize_platform_order_transfer_discount
from ...platform.transfer.platform_order_transfer_product import PlatformOrderTransferProduct, _deserialize_platform_order_transfer_product, _serialize_platform_order_transfer_product

@dataclass
class PlatformOrderTransferOrderLine:
    """주문 항목
    """
    product: PlatformOrderTransferProduct
    """상품
    """
    quantity: int
    """상품 수량
    (int32)
    """
    discounts: list[PlatformOrderTransferDiscount]
    """상품 할인 정보
    """
    additional_fees: list[PlatformOrderTransferAdditionalFee]
    """상품 추가 수수료 정보
    """
    amount: PlatformOrderSettlementAmount
    """상품 정산 금액 정보
    """


def _serialize_platform_order_transfer_order_line(obj: PlatformOrderTransferOrderLine) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["product"] = _serialize_platform_order_transfer_product(obj.product)
    entity["quantity"] = obj.quantity
    entity["discounts"] = list(map(_serialize_platform_order_transfer_discount, obj.discounts))
    entity["additionalFees"] = list(map(_serialize_platform_order_transfer_additional_fee, obj.additional_fees))
    entity["amount"] = _serialize_platform_order_settlement_amount(obj.amount)
    return entity


def _deserialize_platform_order_transfer_order_line(obj: Any) -> PlatformOrderTransferOrderLine:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "product" not in obj:
        raise KeyError(f"'product' is not in {obj}")
    product = obj["product"]
    product = _deserialize_platform_order_transfer_product(product)
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
        item = _deserialize_platform_order_transfer_discount(item)
        discounts[i] = item
    if "additionalFees" not in obj:
        raise KeyError(f"'additionalFees' is not in {obj}")
    additional_fees = obj["additionalFees"]
    if not isinstance(additional_fees, list):
        raise ValueError(f"{repr(additional_fees)} is not list")
    for i, item in enumerate(additional_fees):
        item = _deserialize_platform_order_transfer_additional_fee(item)
        additional_fees[i] = item
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    amount = _deserialize_platform_order_settlement_amount(amount)
    return PlatformOrderTransferOrderLine(product, quantity, discounts, additional_fees, amount)
