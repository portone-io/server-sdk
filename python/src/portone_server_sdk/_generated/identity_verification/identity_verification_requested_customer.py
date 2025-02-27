from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class IdentityVerificationRequestedCustomer:
    """요청 시 고객 정보
    """
    id: Optional[str] = field(default=None)
    """식별 아이디
    """
    name: Optional[str] = field(default=None)
    """이름
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호

    특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
    """
    birth_year: Optional[str] = field(default=None)
    """출생연도
    """
    birth_month: Optional[str] = field(default=None)
    """출생월
    """
    birth_day: Optional[str] = field(default=None)
    """출생일
    """


def _serialize_identity_verification_requested_customer(obj: IdentityVerificationRequestedCustomer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.birth_year is not None:
        entity["birthYear"] = obj.birth_year
    if obj.birth_month is not None:
        entity["birthMonth"] = obj.birth_month
    if obj.birth_day is not None:
        entity["birthDay"] = obj.birth_day
    return entity


def _deserialize_identity_verification_requested_customer(obj: Any) -> IdentityVerificationRequestedCustomer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    if "birthYear" in obj:
        birth_year = obj["birthYear"]
        if not isinstance(birth_year, str):
            raise ValueError(f"{repr(birth_year)} is not str")
    else:
        birth_year = None
    if "birthMonth" in obj:
        birth_month = obj["birthMonth"]
        if not isinstance(birth_month, str):
            raise ValueError(f"{repr(birth_month)} is not str")
    else:
        birth_month = None
    if "birthDay" in obj:
        birth_day = obj["birthDay"]
        if not isinstance(birth_day, str):
            raise ValueError(f"{repr(birth_day)} is not str")
    else:
        birth_day = None
    return IdentityVerificationRequestedCustomer(id, name, phone_number, birth_year, birth_month, birth_day)
