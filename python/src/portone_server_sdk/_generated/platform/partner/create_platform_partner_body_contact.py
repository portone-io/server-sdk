from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreatePlatformPartnerBodyContact:
    """파트너 담당자 정보
    """
    name: str
    """담당자 이름
    """
    email: str
    """담당자 이메일
    """
    phone_number: Optional[str] = field(default=None)
    """담당자 휴대폰 번호
    """


def _serialize_create_platform_partner_body_contact(obj: CreatePlatformPartnerBodyContact) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["email"] = obj.email
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    return entity


def _deserialize_create_platform_partner_body_contact(obj: Any) -> CreatePlatformPartnerBodyContact:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "name" not in obj:
        raise KeyError("Missing required field 'name'")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError("Expected str for name")
    if "email" not in obj:
        raise KeyError("Missing required field 'email'")
    email = obj["email"]
    if not isinstance(email, str):
        raise ValueError("Expected str for email")
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError("Expected str for phone_number")
    else:
        phone_number = None
    return CreatePlatformPartnerBodyContact(name, email, phone_number)
