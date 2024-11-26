from __future__ import annotations
from typing import Any, Literal, Optional, Union

BillingKeyStatus = Union[Literal["ISSUED", "DELETED"], str]
"""빌링키 상태
"""


def _serialize_billing_key_status(obj: BillingKeyStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_billing_key_status(obj: Any) -> BillingKeyStatus:
    return obj
