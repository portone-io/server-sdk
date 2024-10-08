from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class SchedulePlatformPartnersBodyUpdateContact:
    """파트너 업데이트를 위한 유형별 추가 정보
    """
    name: Optional[str]
    """담당자 이름
    """
    phone_number: Optional[str]
    """담당자 휴대폰 번호
    """
    email: Optional[str]
    """담당자 이메일
    """


def _serialize_schedule_platform_partners_body_update_contact(obj: SchedulePlatformPartnersBodyUpdateContact) -> Any:
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.email is not None:
        entity["email"] = obj.email
    return entity


def _deserialize_schedule_platform_partners_body_update_contact(obj: Any) -> SchedulePlatformPartnersBodyUpdateContact:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
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
    if "email" in obj:
        email = obj["email"]
        if not isinstance(email, str):
            raise ValueError(f"{repr(email)} is not str")
    else:
        email = None
    return SchedulePlatformPartnersBodyUpdateContact(name, phone_number, email)
