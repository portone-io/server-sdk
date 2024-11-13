from __future__ import annotations
from typing import Any, Literal, Optional, Union

EasyPayMethodType = Union[Literal["CARD", "TRANSFER", "CHARGE"], str]
"""간편 결제 수단
"""


def _serialize_easy_pay_method_type(obj: EasyPayMethodType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_easy_pay_method_type(obj: Any) -> EasyPayMethodType:
    return obj
