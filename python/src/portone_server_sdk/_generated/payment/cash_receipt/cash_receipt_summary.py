from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CashReceiptSummary:
    """현금영수증 내역
    """
    issue_number: str
    """발행 번호
    """
    url: str
    """현금 영수증 URL
    """
    pg_receipt_id: str
    """PG사 현금영수증 아이디
    """


def _serialize_cash_receipt_summary(obj: CashReceiptSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["issueNumber"] = obj.issue_number
    entity["url"] = obj.url
    entity["pgReceiptId"] = obj.pg_receipt_id
    return entity


def _deserialize_cash_receipt_summary(obj: Any) -> CashReceiptSummary:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "issueNumber" not in obj:
        raise KeyError("Missing required field 'issueNumber'")
    issue_number = obj["issueNumber"]
    if not isinstance(issue_number, str):
        raise ValueError("Expected str for issue_number")
    if "url" not in obj:
        raise KeyError("Missing required field 'url'")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError("Expected str for url")
    if "pgReceiptId" not in obj:
        raise KeyError("Missing required field 'pgReceiptId'")
    pg_receipt_id = obj["pgReceiptId"]
    if not isinstance(pg_receipt_id, str):
        raise ValueError("Expected str for pg_receipt_id")
    return CashReceiptSummary(issue_number, url, pg_receipt_id)
