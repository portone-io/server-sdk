from __future__ import annotations
from typing import Any, Literal, Optional, Union

IssueCashReceiptPaymentMethodType = Union[Literal["TRANSFER", "VIRTUAL_ACCOUNT"], str]
"""현금영수증 발급 가능 결제 수단
"""


def _serialize_issue_cash_receipt_payment_method_type(obj: IssueCashReceiptPaymentMethodType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_issue_cash_receipt_payment_method_type(obj: Any) -> IssueCashReceiptPaymentMethodType:
    return obj
