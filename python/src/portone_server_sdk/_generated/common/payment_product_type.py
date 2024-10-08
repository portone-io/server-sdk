from __future__ import annotations
from typing import Any, Literal, Optional

PaymentProductType = Literal["PHYSICAL", "DIGITAL"]
"""상품 유형
"""


def _serialize_payment_product_type(obj: PaymentProductType) -> Any:
    return obj


def _deserialize_payment_product_type(obj: Any) -> PaymentProductType:
    if obj not in ["PHYSICAL", "DIGITAL"]:
        raise ValueError(f"{repr(obj)} is not PaymentProductType")
    return obj
