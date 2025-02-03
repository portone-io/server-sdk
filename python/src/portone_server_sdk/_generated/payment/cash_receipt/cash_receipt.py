from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.cash_receipt.cancelled_cash_receipt import CancelledCashReceipt, _deserialize_cancelled_cash_receipt, _serialize_cancelled_cash_receipt
from ...payment.cash_receipt.issue_failed_cash_receipt import IssueFailedCashReceipt, _deserialize_issue_failed_cash_receipt, _serialize_issue_failed_cash_receipt
from ...payment.cash_receipt.issued_cash_receipt import IssuedCashReceipt, _deserialize_issued_cash_receipt, _serialize_issued_cash_receipt

CashReceipt = Union[CancelledCashReceipt, IssuedCashReceipt, IssueFailedCashReceipt, dict]
"""현금영수증 내역
"""


def _serialize_cash_receipt(obj: CashReceipt) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, CancelledCashReceipt):
        return _serialize_cancelled_cash_receipt(obj)
    if isinstance(obj, IssuedCashReceipt):
        return _serialize_issued_cash_receipt(obj)
    if isinstance(obj, IssueFailedCashReceipt):
        return _serialize_issue_failed_cash_receipt(obj)


def _deserialize_cash_receipt(obj: Any) -> CashReceipt:
    try:
        return _deserialize_cancelled_cash_receipt(obj)
    except Exception:
        pass
    try:
        return _deserialize_issued_cash_receipt(obj)
    except Exception:
        pass
    try:
        return _deserialize_issue_failed_cash_receipt(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not CashReceipt")
