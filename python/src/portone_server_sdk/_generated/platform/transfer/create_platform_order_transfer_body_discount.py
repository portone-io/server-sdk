from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreatePlatformOrderTransferBodyDiscount:
    """할인 정보
    """
    share_policy_id: str
    """할인 분담 정책 아이디
    """
    amount: int
    """할인 금액
    (int64)
    """
    tax_free_amount: Optional[int] = field(default=None)
    """면세 할인 금액
    (int64)
    """


def _serialize_create_platform_order_transfer_body_discount(obj: CreatePlatformOrderTransferBodyDiscount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["sharePolicyId"] = obj.share_policy_id
    entity["amount"] = obj.amount
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    return entity


def _deserialize_create_platform_order_transfer_body_discount(obj: Any) -> CreatePlatformOrderTransferBodyDiscount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "sharePolicyId" not in obj:
        raise KeyError(f"'sharePolicyId' is not in {obj}")
    share_policy_id = obj["sharePolicyId"]
    if not isinstance(share_policy_id, str):
        raise ValueError(f"{repr(share_policy_id)} is not str")
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError(f"{repr(tax_free_amount)} is not int")
    else:
        tax_free_amount = None
    return CreatePlatformOrderTransferBodyDiscount(share_policy_id, amount, tax_free_amount)
