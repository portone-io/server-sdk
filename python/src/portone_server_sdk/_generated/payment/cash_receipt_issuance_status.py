from __future__ import annotations
from typing import Any, Literal, Optional, Union

CashReceiptIssuanceStatus = Union[Literal["ISSUED", "NOT_ISSUED"], str]
"""현금영수증 발행여부
"""


def _serialize_cash_receipt_issuance_status(obj: CashReceiptIssuanceStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_cash_receipt_issuance_status(obj: Any) -> CashReceiptIssuanceStatus:
    return obj
