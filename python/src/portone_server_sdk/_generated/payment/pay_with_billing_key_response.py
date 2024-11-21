from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.billing_key_payment_summary import BillingKeyPaymentSummary, _deserialize_billing_key_payment_summary, _serialize_billing_key_payment_summary

@dataclass
class PayWithBillingKeyResponse:
    """빌링키 결제 성공 응답
    """
    payment: BillingKeyPaymentSummary
    """결제 건 요약 정보
    """


def _serialize_pay_with_billing_key_response(obj: PayWithBillingKeyResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["payment"] = _serialize_billing_key_payment_summary(obj.payment)
    return entity


def _deserialize_pay_with_billing_key_response(obj: Any) -> PayWithBillingKeyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "payment" not in obj:
        raise KeyError(f"'payment' is not in {obj}")
    payment = obj["payment"]
    payment = _deserialize_billing_key_payment_summary(payment)
    return PayWithBillingKeyResponse(payment)
