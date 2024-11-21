from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.gender import Gender, _deserialize_gender, _serialize_gender
from ..identity_verification.identity_verification_operator import IdentityVerificationOperator, _deserialize_identity_verification_operator, _serialize_identity_verification_operator

@dataclass
class IdentityVerificationVerifiedCustomer:
    """인증된 고객 정보
    """
    name: str
    """이름
    """
    birth_date: str
    """생년월일 (yyyy-MM-dd)

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    id: Optional[str] = field(default=None)
    """식별 아이디
    """
    operator: Optional[IdentityVerificationOperator] = field(default=None)
    """통신사

    다날: 별도 계약이 필요합니다.
    KG이니시스: 제공하지 않습니다.
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호

    특수 문자(-) 없이 숫자로만 이루어진 번호 형식입니다.
    다날: 별도 계약이 필요합니다.
    KG이니시스: 항상 제공합니다.
    """
    gender: Optional[Gender] = field(default=None)
    """성별

    다날: 항상 제공합니다.
    KG이니시스: 항상 제공합니다.
    """
    is_foreigner: Optional[bool] = field(default=None)
    """외국인 여부

    다날: 별도 계약이 필요합니다.
    KG이니시스: 항상 제공합니다.
    """
    ci: Optional[str] = field(default=None)
    """CI (개인 고유 식별키)

    개인을 식별하기 위한 고유 정보입니다.
    다날: 항상 제공합니다.
    KG이니시스: 카카오를 제외한 인증사에서 제공합니다.
    """
    di: Optional[str] = field(default=None)
    """DI (사이트별 개인 고유 식별키)

    중복 가입을 방지하기 위해 개인을 식별하는 사이트별 고유 정보입니다.
    다날: 항상 제공합니다.
    KG이니시스: 제공하지 않습니다.
    """


def _serialize_identity_verification_verified_customer(obj: IdentityVerificationVerifiedCustomer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["birthDate"] = obj.birth_date
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.operator is not None:
        entity["operator"] = _serialize_identity_verification_operator(obj.operator)
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.gender is not None:
        entity["gender"] = _serialize_gender(obj.gender)
    if obj.is_foreigner is not None:
        entity["isForeigner"] = obj.is_foreigner
    if obj.ci is not None:
        entity["ci"] = obj.ci
    if obj.di is not None:
        entity["di"] = obj.di
    return entity


def _deserialize_identity_verification_verified_customer(obj: Any) -> IdentityVerificationVerifiedCustomer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "birthDate" not in obj:
        raise KeyError(f"'birthDate' is not in {obj}")
    birth_date = obj["birthDate"]
    if not isinstance(birth_date, str):
        raise ValueError(f"{repr(birth_date)} is not str")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "operator" in obj:
        operator = obj["operator"]
        operator = _deserialize_identity_verification_operator(operator)
    else:
        operator = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    if "gender" in obj:
        gender = obj["gender"]
        gender = _deserialize_gender(gender)
    else:
        gender = None
    if "isForeigner" in obj:
        is_foreigner = obj["isForeigner"]
        if not isinstance(is_foreigner, bool):
            raise ValueError(f"{repr(is_foreigner)} is not bool")
    else:
        is_foreigner = None
    if "ci" in obj:
        ci = obj["ci"]
        if not isinstance(ci, str):
            raise ValueError(f"{repr(ci)} is not str")
    else:
        ci = None
    if "di" in obj:
        di = obj["di"]
        if not isinstance(di, str):
            raise ValueError(f"{repr(di)} is not str")
    else:
        di = None
    return IdentityVerificationVerifiedCustomer(name, birth_date, id, operator, phone_number, gender, is_foreigner, ci, di)
