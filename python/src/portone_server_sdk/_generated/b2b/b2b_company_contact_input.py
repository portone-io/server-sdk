from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCompanyContactInput:
    id: str
    """담당자 ID

    팝빌 로그인 계정으로 사용됩니다.
    """
    password: str
    """비밀번호
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


def _serialize_b2b_company_contact_input(obj: B2bCompanyContactInput) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["password"] = obj.password
    entity["name"] = obj.name
    entity["phoneNumber"] = obj.phone_number
    entity["email"] = obj.email
    return entity


def _deserialize_b2b_company_contact_input(obj: Any) -> B2bCompanyContactInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "password" not in obj:
        raise KeyError(f"'password' is not in {obj}")
    password = obj["password"]
    if not isinstance(password, str):
        raise ValueError(f"{repr(password)} is not str")
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
    return B2bCompanyContactInput(id, password, name, phone_number, email)
