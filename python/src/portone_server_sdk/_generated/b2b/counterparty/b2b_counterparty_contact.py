from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyContact:
    """거래처 담당자 정보
    """
    name: str
    """담당자 성명
    """
    email: str
    """담당자 이메일
    """
    phone_number: Optional[str] = field(default=None)
    """담당자 전화번호
    """
    memo: Optional[str] = field(default=None)
    """담당자 메모
    """


def _serialize_b2b_counterparty_contact(obj: B2bCounterpartyContact) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["email"] = obj.email
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_b2b_counterparty_contact(obj: Any) -> B2bCounterpartyContact:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "email" not in obj:
        raise KeyError(f"'email' is not in {obj}")
    email = obj["email"]
    if not isinstance(email, str):
        raise ValueError(f"{repr(email)} is not str")
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return B2bCounterpartyContact(name, email, phone_number, memo)
