from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentReconciliationStatus = Union[Literal["MATCHED", "NOT_MATCHED", "INCOMPARABLE", "NOT_COLLECTED"], str]
"""결제 건의 대사 상태
"""


def _serialize_payment_reconciliation_status(obj: PaymentReconciliationStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_reconciliation_status(obj: Any) -> PaymentReconciliationStatus:
    return obj
