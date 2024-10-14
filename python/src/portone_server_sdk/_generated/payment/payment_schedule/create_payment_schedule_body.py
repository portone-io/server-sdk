from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.billing_key_payment_input import BillingKeyPaymentInput, _deserialize_billing_key_payment_input, _serialize_billing_key_payment_input

@dataclass
class CreatePaymentScheduleBody:
    """결제 예약 요청 입력 정보
    """
    payment: BillingKeyPaymentInput
    """빌링키 결제 입력 정보
    """
    time_to_pay: str
    """결제 예정 시점
    (RFC 3339 date-time)
    """


def _serialize_create_payment_schedule_body(obj: CreatePaymentScheduleBody) -> Any:
    entity = {}
    entity["payment"] = _serialize_billing_key_payment_input(obj.payment)
    entity["timeToPay"] = obj.time_to_pay
    return entity


def _deserialize_create_payment_schedule_body(obj: Any) -> CreatePaymentScheduleBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "payment" not in obj:
        raise KeyError(f"'payment' is not in {obj}")
    payment = obj["payment"]
    payment = _deserialize_billing_key_payment_input(payment)
    if "timeToPay" not in obj:
        raise KeyError(f"'timeToPay' is not in {obj}")
    time_to_pay = obj["timeToPay"]
    if not isinstance(time_to_pay, str):
        raise ValueError(f"{repr(time_to_pay)} is not str")
    return CreatePaymentScheduleBody(payment, time_to_pay)
