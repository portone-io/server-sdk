from __future__ import annotations
from typing import Any, Literal, Optional

PaymentMethodVirtualAccountType = Literal["FIXED", "NORMAL"]
"""가상계좌 유형
"""


def _serialize_payment_method_virtual_account_type(obj: PaymentMethodVirtualAccountType) -> Any:
    return obj


def _deserialize_payment_method_virtual_account_type(obj: Any) -> PaymentMethodVirtualAccountType:
    if obj not in ["FIXED", "NORMAL"]:
        raise ValueError(f"{repr(obj)} is not PaymentMethodVirtualAccountType")
    return obj
