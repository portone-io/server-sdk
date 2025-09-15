from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmedBillingKeyIssueAndPaySummary:
    """빌링키 발급 및 초회 결제 수동 승인 완료 응답
    """
    billing_key: str
    """빌링키
    """
    payment_id: str
    """결제 건 아이디
    """


def _serialize_confirmed_billing_key_issue_and_pay_summary(obj: ConfirmedBillingKeyIssueAndPaySummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["billingKey"] = obj.billing_key
    entity["paymentId"] = obj.payment_id
    return entity


def _deserialize_confirmed_billing_key_issue_and_pay_summary(obj: Any) -> ConfirmedBillingKeyIssueAndPaySummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    return ConfirmedBillingKeyIssueAndPaySummary(billing_key, payment_id)
