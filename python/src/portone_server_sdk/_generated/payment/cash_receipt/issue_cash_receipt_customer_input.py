from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class IssueCashReceiptCustomerInput:
    """현금영수증 발급 시 고객 관련 입력 정보
    """
    identity_number: str
    """고객 식별값
    """
    name: Optional[str] = field(default=None)
    """이름
    """
    email: Optional[str] = field(default=None)
    """이메일
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호
    """


def _serialize_issue_cash_receipt_customer_input(obj: IssueCashReceiptCustomerInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["identityNumber"] = obj.identity_number
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.email is not None:
        entity["email"] = obj.email
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    return entity


def _deserialize_issue_cash_receipt_customer_input(obj: Any) -> IssueCashReceiptCustomerInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "identityNumber" not in obj:
        raise KeyError(f"'identityNumber' is not in {obj}")
    identity_number = obj["identityNumber"]
    if not isinstance(identity_number, str):
        raise ValueError(f"{repr(identity_number)} is not str")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "email" in obj:
        email = obj["email"]
        if not isinstance(email, str):
            raise ValueError(f"{repr(email)} is not str")
    else:
        email = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    return IssueCashReceiptCustomerInput(identity_number, name, email, phone_number)
