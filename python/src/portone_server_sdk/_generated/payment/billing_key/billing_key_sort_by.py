from __future__ import annotations
from typing import Any, Literal, Optional, Union

BillingKeySortBy = Union[Literal["REQUESTED_AT", "ISSUED_AT", "DELETED_AT", "STATUS_TIMESTAMP"], str]
"""빌링키 정렬 기준
"""


def _serialize_billing_key_sort_by(obj: BillingKeySortBy) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_billing_key_sort_by(obj: Any) -> BillingKeySortBy:
    return obj
