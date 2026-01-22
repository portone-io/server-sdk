from __future__ import annotations
from typing import Any, Literal, Optional, Union

IssueCashReceiptCustomerInputIdentityNumberType = Union[Literal["PHONE", "CARD", "BUSINESS"], str]
"""현금영수증 발급 시 고객 식별 정보 유형
"""


def _serialize_issue_cash_receipt_customer_input_identity_number_type(obj: IssueCashReceiptCustomerInputIdentityNumberType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_issue_cash_receipt_customer_input_identity_number_type(obj: Any) -> IssueCashReceiptCustomerInputIdentityNumberType:
    return obj
