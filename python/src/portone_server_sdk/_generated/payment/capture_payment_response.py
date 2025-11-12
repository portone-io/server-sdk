from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CapturePaymentResponse:
    """수동 매입 성공 응답
    """
    pass


def _serialize_capture_payment_response(obj: CapturePaymentResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_capture_payment_response(obj: Any) -> CapturePaymentResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return CapturePaymentResponse()
