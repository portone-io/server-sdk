from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentMethodVirtualAccountType = Union[Literal["FIXED", "NORMAL"], str]
"""가상계좌 유형
"""


def _serialize_payment_method_virtual_account_type(obj: PaymentMethodVirtualAccountType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_method_virtual_account_type(obj: Any) -> PaymentMethodVirtualAccountType:
    return obj
