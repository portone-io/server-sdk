from __future__ import annotations
from typing import Any, Literal, Optional, Union

InstantPaymentMethodInputVirtualAccountOptionType = Union[Literal["NORMAL", "FIXED"], str]
"""가상계좌 발급 유형
"""


def _serialize_instant_payment_method_input_virtual_account_option_type(obj: InstantPaymentMethodInputVirtualAccountOptionType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_instant_payment_method_input_virtual_account_option_type(obj: Any) -> InstantPaymentMethodInputVirtualAccountOptionType:
    return obj
