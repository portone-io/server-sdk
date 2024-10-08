from __future__ import annotations
from typing import Any, Literal, Optional

InstantPaymentMethodInputVirtualAccountOptionType = Literal["NORMAL", "FIXED"]
"""가상계좌 발급 유형
"""


def _serialize_instant_payment_method_input_virtual_account_option_type(obj: InstantPaymentMethodInputVirtualAccountOptionType) -> Any:
    return obj


def _deserialize_instant_payment_method_input_virtual_account_option_type(obj: Any) -> InstantPaymentMethodInputVirtualAccountOptionType:
    if obj not in ["NORMAL", "FIXED"]:
        raise ValueError(f"{repr(obj)} is not InstantPaymentMethodInputVirtualAccountOptionType")
    return obj
