from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentFailure:
    """결제 실패 정보
    """
    reason: Optional[str]
    """실패 사유
    """
    pg_code: Optional[str]
    """PG사 실패 코드
    """
    pg_message: Optional[str]
    """PG사 실패 메시지
    """


def _serialize_payment_failure(obj: PaymentFailure) -> Any:
    entity = {}
    if obj.reason is not None:
        entity["reason"] = obj.reason
    if obj.pg_code is not None:
        entity["pgCode"] = obj.pg_code
    if obj.pg_message is not None:
        entity["pgMessage"] = obj.pg_message
    return entity


def _deserialize_payment_failure(obj: Any) -> PaymentFailure:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "reason" in obj:
        reason = obj["reason"]
        if not isinstance(reason, str):
            raise ValueError(f"{repr(reason)} is not str")
    else:
        reason = None
    if "pgCode" in obj:
        pg_code = obj["pgCode"]
        if not isinstance(pg_code, str):
            raise ValueError(f"{repr(pg_code)} is not str")
    else:
        pg_code = None
    if "pgMessage" in obj:
        pg_message = obj["pgMessage"]
        if not isinstance(pg_message, str):
            raise ValueError(f"{repr(pg_message)} is not str")
    else:
        pg_message = None
    return PaymentFailure(reason, pg_code, pg_message)
