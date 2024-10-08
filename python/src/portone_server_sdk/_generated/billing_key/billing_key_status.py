from __future__ import annotations
from typing import Any, Literal, Optional

BillingKeyStatus = Literal["ISSUED", "DELETED"]
"""빌링키 상태
"""


def _serialize_billing_key_status(obj: BillingKeyStatus) -> Any:
    return obj


def _deserialize_billing_key_status(obj: Any) -> BillingKeyStatus:
    if obj not in ["ISSUED", "DELETED"]:
        raise ValueError(f"{repr(obj)} is not BillingKeyStatus")
    return obj
