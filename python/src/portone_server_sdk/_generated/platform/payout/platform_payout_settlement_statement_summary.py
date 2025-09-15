from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.payout.platform_payout_settlement_statement_status import PlatformPayoutSettlementStatementStatus, _deserialize_platform_payout_settlement_statement_status, _serialize_platform_payout_settlement_statement_status

@dataclass
class PlatformPayoutSettlementStatementSummary:
    """정산 내역서 요약 정보
    """
    status: PlatformPayoutSettlementStatementStatus
    """상태
    """
    id: Optional[str] = field(default=None)
    """아이디
    """
    issued_at: Optional[str] = field(default=None)
    """발송 일시
    (RFC 3339 date-time)
    """


def _serialize_platform_payout_settlement_statement_summary(obj: PlatformPayoutSettlementStatementSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = _serialize_platform_payout_settlement_statement_status(obj.status)
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.issued_at is not None:
        entity["issuedAt"] = obj.issued_at
    return entity


def _deserialize_platform_payout_settlement_statement_summary(obj: Any) -> PlatformPayoutSettlementStatementSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_payout_settlement_statement_status(status)
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "issuedAt" in obj:
        issued_at = obj["issuedAt"]
        if not isinstance(issued_at, str):
            raise ValueError(f"{repr(issued_at)} is not str")
    else:
        issued_at = None
    return PlatformPayoutSettlementStatementSummary(status, id, issued_at)
