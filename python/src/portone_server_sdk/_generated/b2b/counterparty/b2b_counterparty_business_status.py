from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bCounterpartyBusinessStatus = Union[Literal["UNKNOWN", "IN_BUSINESS", "CLOSED", "SUSPENDED", "NOT_FOUND", "CHECK_PENDING", "CHECK_FAILED"], str]
"""거래처 휴폐업 상태
"""


def _serialize_b2b_counterparty_business_status(obj: B2bCounterpartyBusinessStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_counterparty_business_status(obj: Any) -> B2bCounterpartyBusinessStatus:
    return obj
