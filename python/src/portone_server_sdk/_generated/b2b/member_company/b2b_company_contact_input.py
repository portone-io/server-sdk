from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCompanyContactInput:
    """담당자 관련 입력 정보
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
    login_id: Optional[str]
    """담당자 계정 ID

    팝빌 로그인 계정으로 사용됩니다.
    값을 입력하지 않을 경우 자동 채번됩니다.
    """
    password: Optional[str]
    """비밀번호

    값을 입력하지 않을 경우 자동 채번됩니다.
    """


def _serialize_b2b_company_contact_input(obj: B2bCompanyContactInput) -> Any:
    entity = {}
    entity["name"] = obj.name
    entity["phoneNumber"] = obj.phone_number
    entity["email"] = obj.email
    if obj.login_id is not None:
        entity["loginId"] = obj.login_id
    if obj.password is not None:
        entity["password"] = obj.password
    return entity


def _deserialize_b2b_company_contact_input(obj: Any) -> B2bCompanyContactInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
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
    if "loginId" in obj:
        login_id = obj["loginId"]
        if not isinstance(login_id, str):
            raise ValueError(f"{repr(login_id)} is not str")
    else:
        login_id = None
    if "password" in obj:
        password = obj["password"]
        if not isinstance(password, str):
            raise ValueError(f"{repr(password)} is not str")
    else:
        password = None
    return B2bCompanyContactInput(name, phone_number, email, login_id, password)
