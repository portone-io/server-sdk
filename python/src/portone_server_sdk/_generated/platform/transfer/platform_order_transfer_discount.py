from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_discount_share_policy import PlatformDiscountSharePolicy, _deserialize_platform_discount_share_policy, _serialize_platform_discount_share_policy

@dataclass
class PlatformOrderTransferDiscount:
    """할인 정보
    """
    share_policy: PlatformDiscountSharePolicy
    """할인 분담 정책
    """
    amount: int
    """할인 금액
    (int64)
    """
    tax_free_amount: int
    """면세 할인 금액
    (int64)
    """
    share_amount: int
    """할인 분담 금액
    (int64)
    """
    share_tax_free_amount: int
    """면세 할인 분담 금액
    (int64)
    """


def _serialize_platform_order_transfer_discount(obj: PlatformOrderTransferDiscount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["sharePolicy"] = _serialize_platform_discount_share_policy(obj.share_policy)
    entity["amount"] = obj.amount
    entity["taxFreeAmount"] = obj.tax_free_amount
    entity["shareAmount"] = obj.share_amount
    entity["shareTaxFreeAmount"] = obj.share_tax_free_amount
    return entity


def _deserialize_platform_order_transfer_discount(obj: Any) -> PlatformOrderTransferDiscount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "sharePolicy" not in obj:
        raise KeyError(f"'sharePolicy' is not in {obj}")
    share_policy = obj["sharePolicy"]
    share_policy = _deserialize_platform_discount_share_policy(share_policy)
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "taxFreeAmount" not in obj:
        raise KeyError(f"'taxFreeAmount' is not in {obj}")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError(f"{repr(tax_free_amount)} is not int")
    if "shareAmount" not in obj:
        raise KeyError(f"'shareAmount' is not in {obj}")
    share_amount = obj["shareAmount"]
    if not isinstance(share_amount, int):
        raise ValueError(f"{repr(share_amount)} is not int")
    if "shareTaxFreeAmount" not in obj:
        raise KeyError(f"'shareTaxFreeAmount' is not in {obj}")
    share_tax_free_amount = obj["shareTaxFreeAmount"]
    if not isinstance(share_tax_free_amount, int):
        raise ValueError(f"{repr(share_tax_free_amount)} is not int")
    return PlatformOrderTransferDiscount(share_policy, amount, tax_free_amount, share_amount, share_tax_free_amount)
