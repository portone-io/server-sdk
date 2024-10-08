from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class InstantPaymentSummary:
    """수기 결제가 완료된 결제 건 요약 정보
    """
    pg_tx_id: str
    """PG사 결제 아이디
    """
    paid_at: str
    """결제 완료 시점
    (RFC 3339 date-time)
    """


def _serialize_instant_payment_summary(obj: InstantPaymentSummary) -> Any:
    entity = {}
    entity["pgTxId"] = obj.pg_tx_id
    entity["paidAt"] = obj.paid_at
    return entity


def _deserialize_instant_payment_summary(obj: Any) -> InstantPaymentSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "pgTxId" not in obj:
        raise KeyError(f"'pgTxId' is not in {obj}")
    pg_tx_id = obj["pgTxId"]
    if not isinstance(pg_tx_id, str):
        raise ValueError(f"{repr(pg_tx_id)} is not str")
    if "paidAt" not in obj:
        raise KeyError(f"'paidAt' is not in {obj}")
    paid_at = obj["paidAt"]
    if not isinstance(paid_at, str):
        raise ValueError(f"{repr(paid_at)} is not str")
    return InstantPaymentSummary(pg_tx_id, paid_at)
