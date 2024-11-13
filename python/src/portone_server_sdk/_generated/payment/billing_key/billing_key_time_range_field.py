from __future__ import annotations
from typing import Any, Literal, Optional, Union

BillingKeyTimeRangeField = Union[Literal["REQUESTED_AT", "ISSUED_AT", "DELETED_AT", "STATUS_TIMESTAMP"], str]
"""빌링키 다건 조회 시, 시각 범위를 적용할 필드
"""


def _serialize_billing_key_time_range_field(obj: BillingKeyTimeRangeField) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_billing_key_time_range_field(obj: Any) -> BillingKeyTimeRangeField:
    return obj
