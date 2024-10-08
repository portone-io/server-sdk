from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class IdentityVerificationRequestedCustomer:
    """요청 시 고객 정보
    """
    id: Optional[str]
    """식별 아이디
    """
    name: Optional[str]
    """이름
    """
    phone_number: Optional[str]
    """전화번호

    특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
    """


def _serialize_identity_verification_requested_customer(obj: IdentityVerificationRequestedCustomer) -> Any:
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
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
    return IdentityVerificationRequestedCustomer(id, name, phone_number)
