from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformContact:
    """플랫폼 파트너 담당자 연락 정보

    파트너 담당자에게 연락하기 위한 정보들 입니다.
    """
    name: str
    """담당자 이름
    """
    email: str
    """담당자 이메일
    """
    phone_number: Optional[str]
    """담당자 휴대폰 번호
    """


def _serialize_platform_contact(obj: PlatformContact) -> Any:
    entity = {}
    entity["name"] = obj.name
    entity["email"] = obj.email
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    return entity


def _deserialize_platform_contact(obj: Any) -> PlatformContact:
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
    return PlatformContact(name, email, phone_number)
