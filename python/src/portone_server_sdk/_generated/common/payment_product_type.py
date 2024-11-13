from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentProductType = Union[Literal["PHYSICAL", "DIGITAL"], str]
"""상품 유형
"""


def _serialize_payment_product_type(obj: PaymentProductType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_product_type(obj: Any) -> PaymentProductType:
    return obj
