from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.cash_receipt.cash_receipt_summary import CashReceiptSummary, _deserialize_cash_receipt_summary, _serialize_cash_receipt_summary

@dataclass
class IssueCashReceiptResponse:
    """현금 영수증 발급 성공 응답
    """
    cash_receipt: CashReceiptSummary


def _serialize_issue_cash_receipt_response(obj: IssueCashReceiptResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["cashReceipt"] = _serialize_cash_receipt_summary(obj.cash_receipt)
    return entity


def _deserialize_issue_cash_receipt_response(obj: Any) -> IssueCashReceiptResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "cashReceipt" not in obj:
        raise KeyError(f"'cashReceipt' is not in {obj}")
    cash_receipt = obj["cashReceipt"]
    cash_receipt = _deserialize_cash_receipt_summary(cash_receipt)
    return IssueCashReceiptResponse(cash_receipt)
