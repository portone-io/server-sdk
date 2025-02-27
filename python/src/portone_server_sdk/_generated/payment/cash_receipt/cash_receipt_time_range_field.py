from __future__ import annotations
from typing import Any, Literal, Optional, Union

CashReceiptTimeRangeField = Union[Literal["ISSUED_AT", "CANCELLED_AT", "STATUS_UPDATED_AT"], str]
"""현금영수증 다건 조회 시, 시각 범위를 적용할 필드
"""


def _serialize_cash_receipt_time_range_field(obj: CashReceiptTimeRangeField) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_cash_receipt_time_range_field(obj: Any) -> CashReceiptTimeRangeField:
    return obj
