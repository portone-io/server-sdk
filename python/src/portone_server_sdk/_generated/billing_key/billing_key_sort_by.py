from __future__ import annotations
from typing import Any, Literal, Optional

BillingKeySortBy = Literal["REQUESTED_AT", "ISSUED_AT", "DELETED_AT", "STATUS_TIMESTAMP"]
"""빌링키 정렬 기준
"""


def _serialize_billing_key_sort_by(obj: BillingKeySortBy) -> Any:
    return obj


def _deserialize_billing_key_sort_by(obj: Any) -> BillingKeySortBy:
    if obj not in ["REQUESTED_AT", "ISSUED_AT", "DELETED_AT", "STATUS_TIMESTAMP"]:
        raise ValueError(f"{repr(obj)} is not BillingKeySortBy")
    return obj
