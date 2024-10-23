from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCompanyContact:
    """담당자 정보
    """
    login_id: str
    """담당자 계정 ID

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
    is_admin: bool
    """관리자 여부

    true일 경우 관리자 권한, false일 경우 일반 권한 담당자입니다.
    """


def _serialize_b2b_company_contact(obj: B2bCompanyContact) -> Any:
    entity = {}
    entity["loginId"] = obj.login_id
    entity["name"] = obj.name
    entity["phoneNumber"] = obj.phone_number
    entity["email"] = obj.email
    entity["registeredAt"] = obj.registered_at
    entity["isAdmin"] = obj.is_admin
    return entity


def _deserialize_b2b_company_contact(obj: Any) -> B2bCompanyContact:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "loginId" not in obj:
        raise KeyError(f"'loginId' is not in {obj}")
    login_id = obj["loginId"]
    if not isinstance(login_id, str):
        raise ValueError(f"{repr(login_id)} is not str")
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
    if "isAdmin" not in obj:
        raise KeyError(f"'isAdmin' is not in {obj}")
    is_admin = obj["isAdmin"]
    if not isinstance(is_admin, bool):
        raise ValueError(f"{repr(is_admin)} is not bool")
    return B2bCompanyContact(login_id, name, phone_number, email, registered_at, is_admin)
