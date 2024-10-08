from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCompanyContact:
    id: str
    """담당자 ID

    팝빌 로그인 계정으로 사용됩니다.
    """
    name: str
    """담당자 성명
    """
    phone_number: str
    """담당자 핸드폰 번호
    """
    email: str
    """담당자 이메일
    """
    registered_at: str
    """등록 일시
    (RFC 3339 date-time)
    """
    is_manager: bool
    """관리자 여부

    true일 경우 관리자, false일 경우 담당자입니다.
    """


def _serialize_b2b_company_contact(obj: B2bCompanyContact) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["name"] = obj.name
    entity["phoneNumber"] = obj.phone_number
    entity["email"] = obj.email
    entity["registeredAt"] = obj.registered_at
    entity["isManager"] = obj.is_manager
    return entity


def _deserialize_b2b_company_contact(obj: Any) -> B2bCompanyContact:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "phoneNumber" not in obj:
        raise KeyError(f"'phoneNumber' is not in {obj}")
    phone_number = obj["phoneNumber"]
    if not isinstance(phone_number, str):
        raise ValueError(f"{repr(phone_number)} is not str")
    if "email" not in obj:
        raise KeyError(f"'email' is not in {obj}")
    email = obj["email"]
    if not isinstance(email, str):
        raise ValueError(f"{repr(email)} is not str")
    if "registeredAt" not in obj:
        raise KeyError(f"'registeredAt' is not in {obj}")
    registered_at = obj["registeredAt"]
    if not isinstance(registered_at, str):
        raise ValueError(f"{repr(registered_at)} is not str")
    if "isManager" not in obj:
        raise KeyError(f"'isManager' is not in {obj}")
    is_manager = obj["isManager"]
    if not isinstance(is_manager, bool):
        raise ValueError(f"{repr(is_manager)} is not bool")
    return B2bCompanyContact(id, name, phone_number, email, registered_at, is_manager)
