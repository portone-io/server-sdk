from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CardCredential:
    """카드 인증 관련 정보
    """
    number: str
    """카드 번호 (숫자만)
    """
    expiry_year: str
    """유효 기간 만료 연도 (2자리)
    """
    expiry_month: str
    """유효 기간 만료 월 (2자리)
    """
    birth_or_business_registration_number: Optional[str]
    """생년월일 (yyMMdd) 또는 사업자 등록 번호 (10자리, 숫자만)
    """
    password_two_digits: Optional[str]
    """비밀번호 앞 2자리
    """


def _serialize_card_credential(obj: CardCredential) -> Any:
    entity = {}
    entity["number"] = obj.number
    entity["expiryYear"] = obj.expiry_year
    entity["expiryMonth"] = obj.expiry_month
    if obj.birth_or_business_registration_number is not None:
        entity["birthOrBusinessRegistrationNumber"] = obj.birth_or_business_registration_number
    if obj.password_two_digits is not None:
        entity["passwordTwoDigits"] = obj.password_two_digits
    return entity


def _deserialize_card_credential(obj: Any) -> CardCredential:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "number" not in obj:
        raise KeyError(f"'number' is not in {obj}")
    number = obj["number"]
    if not isinstance(number, str):
        raise ValueError(f"{repr(number)} is not str")
    if "expiryYear" not in obj:
        raise KeyError(f"'expiryYear' is not in {obj}")
    expiry_year = obj["expiryYear"]
    if not isinstance(expiry_year, str):
        raise ValueError(f"{repr(expiry_year)} is not str")
    if "expiryMonth" not in obj:
        raise KeyError(f"'expiryMonth' is not in {obj}")
    expiry_month = obj["expiryMonth"]
    if not isinstance(expiry_month, str):
        raise ValueError(f"{repr(expiry_month)} is not str")
    if "birthOrBusinessRegistrationNumber" in obj:
        birth_or_business_registration_number = obj["birthOrBusinessRegistrationNumber"]
        if not isinstance(birth_or_business_registration_number, str):
            raise ValueError(f"{repr(birth_or_business_registration_number)} is not str")
    else:
        birth_or_business_registration_number = None
    if "passwordTwoDigits" in obj:
        password_two_digits = obj["passwordTwoDigits"]
        if not isinstance(password_two_digits, str):
            raise ValueError(f"{repr(password_two_digits)} is not str")
    else:
        password_two_digits = None
    return CardCredential(number, expiry_year, expiry_month, birth_or_business_registration_number, password_two_digits)
