from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.instant_payment_summary import InstantPaymentSummary, _deserialize_instant_payment_summary, _serialize_instant_payment_summary

@dataclass
class PayInstantlyResponse:
    """수기 결제 성공 응답
    """
    payment: InstantPaymentSummary
    """결제 건 요약 정보
    """


def _serialize_pay_instantly_response(obj: PayInstantlyResponse) -> Any:
    entity = {}
    entity["payment"] = _serialize_instant_payment_summary(obj.payment)
    return entity


def _deserialize_pay_instantly_response(obj: Any) -> PayInstantlyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "payment" not in obj:
        raise KeyError(f"'payment' is not in {obj}")
    payment = obj["payment"]
    payment = _deserialize_instant_payment_summary(payment)
    return PayInstantlyResponse(payment)
