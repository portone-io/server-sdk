from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyFailure:
    """발급 실패 상세 정보
    """
    failed_at: str
    """실패 시점
    (RFC 3339 date-time)
    """
    message: Optional[str] = field(default=None)
    """실패 사유
    """
    pg_code: Optional[str] = field(default=None)
    """PG사 실패 코드
    """
    pg_message: Optional[str] = field(default=None)
    """PG사 실패 사유
    """


def _serialize_billing_key_failure(obj: BillingKeyFailure) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["failedAt"] = obj.failed_at
    if obj.message is not None:
        entity["message"] = obj.message
    if obj.pg_code is not None:
        entity["pgCode"] = obj.pg_code
    if obj.pg_message is not None:
        entity["pgMessage"] = obj.pg_message
    return entity


def _deserialize_billing_key_failure(obj: Any) -> BillingKeyFailure:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "failedAt" not in obj:
        raise KeyError("Missing required field 'failedAt'")
    failed_at = obj["failedAt"]
    if not isinstance(failed_at, str):
        raise ValueError("Expected str for failed_at")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    if "pgCode" in obj:
        pg_code = obj["pgCode"]
        if not isinstance(pg_code, str):
            raise ValueError("Expected str for pg_code")
    else:
        pg_code = None
    if "pgMessage" in obj:
        pg_message = obj["pgMessage"]
        if not isinstance(pg_message, str):
            raise ValueError("Expected str for pg_message")
    else:
        pg_message = None
    return BillingKeyFailure(failed_at, message, pg_code, pg_message)
