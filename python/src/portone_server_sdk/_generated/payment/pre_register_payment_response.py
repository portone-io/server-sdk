from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PreRegisterPaymentResponse:
    """결제 사전 등록 성공 응답
    """
    pass


def _serialize_pre_register_payment_response(obj: PreRegisterPaymentResponse) -> Any:
    entity = {}
    return entity


def _deserialize_pre_register_payment_response(obj: Any) -> PreRegisterPaymentResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return PreRegisterPaymentResponse()
