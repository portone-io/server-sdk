from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyVerification:
    """거래처 검증 정보
    """
    id: str
    """외부 API 사용 ID
    """
    checked_at: str
    """검증 시각
    (RFC 3339 date-time)
    """


def _serialize_b2b_counterparty_verification(obj: B2bCounterpartyVerification) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["checkedAt"] = obj.checked_at
    return entity


def _deserialize_b2b_counterparty_verification(obj: Any) -> B2bCounterpartyVerification:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "checkedAt" not in obj:
        raise KeyError("Missing required field 'checkedAt'")
    checked_at = obj["checkedAt"]
    if not isinstance(checked_at, str):
        raise ValueError("Expected str for checked_at")
    return B2bCounterpartyVerification(id, checked_at)
