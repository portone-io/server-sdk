from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.cash_receipt_type import CashReceiptType, _deserialize_cash_receipt_type, _serialize_cash_receipt_type
from ..common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class CancelledPaymentCashReceipt:
    """취소된 현금영수증
    """
    """결제 건 내 현금영수증 상태
    """
    issue_number: str
    """승인 번호
    """
    total_amount: int
    """총 금액
    (int64)
    """
    currency: Currency
    """통화
    """
    issued_at: str
    """발급 시점
    (RFC 3339 date-time)
    """
    cancelled_at: str
    """취소 시점
    (RFC 3339 date-time)
    """
    type: Optional[CashReceiptType] = field(default=None)
    """현금영수증 유형
    """
    pg_receipt_id: Optional[str] = field(default=None)
    """PG사 영수증 발급 아이디
    """
    tax_free_amount: Optional[int] = field(default=None)
    """면세액
    (int64)
    """
    url: Optional[str] = field(default=None)
    """현금영수증 URL
    """


def _serialize_cancelled_payment_cash_receipt(obj: CancelledPaymentCashReceipt) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "CANCELLED"
    entity["issueNumber"] = obj.issue_number
    entity["totalAmount"] = obj.total_amount
    entity["currency"] = _serialize_currency(obj.currency)
    entity["issuedAt"] = obj.issued_at
    entity["cancelledAt"] = obj.cancelled_at
    if obj.type is not None:
        entity["type"] = _serialize_cash_receipt_type(obj.type)
    if obj.pg_receipt_id is not None:
        entity["pgReceiptId"] = obj.pg_receipt_id
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.url is not None:
        entity["url"] = obj.url
    return entity


def _deserialize_cancelled_payment_cash_receipt(obj: Any) -> CancelledPaymentCashReceipt:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "CANCELLED":
        raise ValueError(f"{repr(status)} is not 'CANCELLED'")
    if "issueNumber" not in obj:
        raise KeyError(f"'issueNumber' is not in {obj}")
    issue_number = obj["issueNumber"]
    if not isinstance(issue_number, str):
        raise ValueError(f"{repr(issue_number)} is not str")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "issuedAt" not in obj:
        raise KeyError(f"'issuedAt' is not in {obj}")
    issued_at = obj["issuedAt"]
    if not isinstance(issued_at, str):
        raise ValueError(f"{repr(issued_at)} is not str")
    if "cancelledAt" not in obj:
        raise KeyError(f"'cancelledAt' is not in {obj}")
    cancelled_at = obj["cancelledAt"]
    if not isinstance(cancelled_at, str):
        raise ValueError(f"{repr(cancelled_at)} is not str")
    if "type" in obj:
        type = obj["type"]
        type = _deserialize_cash_receipt_type(type)
    else:
        type = None
    if "pgReceiptId" in obj:
        pg_receipt_id = obj["pgReceiptId"]
        if not isinstance(pg_receipt_id, str):
            raise ValueError(f"{repr(pg_receipt_id)} is not str")
    else:
        pg_receipt_id = None
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError(f"{repr(tax_free_amount)} is not int")
    else:
        tax_free_amount = None
    if "url" in obj:
        url = obj["url"]
        if not isinstance(url, str):
            raise ValueError(f"{repr(url)} is not str")
    else:
        url = None
    return CancelledPaymentCashReceipt(issue_number, total_amount, currency, issued_at, cancelled_at, type, pg_receipt_id, tax_free_amount, url)
