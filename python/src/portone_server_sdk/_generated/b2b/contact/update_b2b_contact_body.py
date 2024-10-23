from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class UpdateB2bContactBody:
    """담당자 정보 수정 요청
    """
    password: Optional[str]
    """비밀번호
    """
    name: Optional[str]
    """담당자 성명
    """
    phone_number: Optional[str]
    """담당자 핸드폰 번호
    """
    email: Optional[str]
    """담당자 이메일
    """


def _serialize_update_b2b_contact_body(obj: UpdateB2bContactBody) -> Any:
    entity = {}
    if obj.password is not None:
        entity["password"] = obj.password
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.email is not None:
        entity["email"] = obj.email
    return entity


def _deserialize_update_b2b_contact_body(obj: Any) -> UpdateB2bContactBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "password" in obj:
        password = obj["password"]
        if not isinstance(password, str):
            raise ValueError(f"{repr(password)} is not str")
    else:
        password = None
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
    return UpdateB2bContactBody(password, name, phone_number, email)
