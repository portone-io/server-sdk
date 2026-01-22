from __future__ import annotations
from typing import Any, Literal, Optional, Union

SimplifiedPaymentMethodType = Union[Literal["CARD", "VIRTUAL_ACCOUNT", "TRANSFER", "CHARGE", "MOBILE", "POINT", "ETC"], str]
"""간소화된 결제수단 목록
"""


def _serialize_simplified_payment_method_type(obj: SimplifiedPaymentMethodType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_simplified_payment_method_type(obj: Any) -> SimplifiedPaymentMethodType:
    return obj
