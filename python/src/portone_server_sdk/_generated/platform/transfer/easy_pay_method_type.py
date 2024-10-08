from __future__ import annotations
from typing import Any, Literal, Optional

EasyPayMethodType = Literal["CARD", "TRANSFER", "CHARGE"]
"""간편 결제 수단
"""


def _serialize_easy_pay_method_type(obj: EasyPayMethodType) -> Any:
    return obj


def _deserialize_easy_pay_method_type(obj: Any) -> EasyPayMethodType:
    if obj not in ["CARD", "TRANSFER", "CHARGE"]:
        raise ValueError(f"{repr(obj)} is not EasyPayMethodType")
    return obj
