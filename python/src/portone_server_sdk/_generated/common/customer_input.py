from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.country import Country, _deserialize_country, _serialize_country
from ..common.customer_name_input import CustomerNameInput, _deserialize_customer_name_input, _serialize_customer_name_input
from ..common.gender import Gender, _deserialize_gender, _serialize_gender
from ..common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input

@dataclass
class CustomerInput:
    """고객 정보 입력 정보
    """
    id: Optional[str] = field(default=None)
    """고객 아이디

    고객사가 지정한 고객의 고유 식별자입니다.
    """
    name: Optional[CustomerNameInput] = field(default=None)
    """이름
    """
    birth_year: Optional[str] = field(default=None)
    """출생 연도
    """
    birth_month: Optional[str] = field(default=None)
    """출생월
    """
    birth_day: Optional[str] = field(default=None)
    """출생일
    """
    country: Optional[Country] = field(default=None)
    """국가
    """
    gender: Optional[Gender] = field(default=None)
    """성별
    """
    email: Optional[str] = field(default=None)
    """이메일
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호
    """
    address: Optional[SeparatedAddressInput] = field(default=None)
    """주소
    """
    zipcode: Optional[str] = field(default=None)
    """우편번호
    """
    business_registration_number: Optional[str] = field(default=None)
    """사업자 등록 번호
    """


def _serialize_customer_input(obj: CustomerInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.name is not None:
        entity["name"] = _serialize_customer_name_input(obj.name)
    if obj.birth_year is not None:
        entity["birthYear"] = obj.birth_year
    if obj.birth_month is not None:
        entity["birthMonth"] = obj.birth_month
    if obj.birth_day is not None:
        entity["birthDay"] = obj.birth_day
    if obj.country is not None:
        entity["country"] = _serialize_country(obj.country)
    if obj.gender is not None:
        entity["gender"] = _serialize_gender(obj.gender)
    if obj.email is not None:
        entity["email"] = obj.email
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.address is not None:
        entity["address"] = _serialize_separated_address_input(obj.address)
    if obj.zipcode is not None:
        entity["zipcode"] = obj.zipcode
    if obj.business_registration_number is not None:
        entity["businessRegistrationNumber"] = obj.business_registration_number
    return entity


def _deserialize_customer_input(obj: Any) -> CustomerInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "name" in obj:
        name = obj["name"]
        name = _deserialize_customer_name_input(name)
    else:
        name = None
    if "birthYear" in obj:
        birth_year = obj["birthYear"]
        if not isinstance(birth_year, str):
            raise ValueError(f"{repr(birth_year)} is not str")
    else:
        birth_year = None
    if "birthMonth" in obj:
        birth_month = obj["birthMonth"]
        if not isinstance(birth_month, str):
            raise ValueError(f"{repr(birth_month)} is not str")
    else:
        birth_month = None
    if "birthDay" in obj:
        birth_day = obj["birthDay"]
        if not isinstance(birth_day, str):
            raise ValueError(f"{repr(birth_day)} is not str")
    else:
        birth_day = None
    if "country" in obj:
        country = obj["country"]
        country = _deserialize_country(country)
    else:
        country = None
    if "gender" in obj:
        gender = obj["gender"]
        gender = _deserialize_gender(gender)
    else:
        gender = None
    if "email" in obj:
        email = obj["email"]
        if not isinstance(email, str):
            raise ValueError(f"{repr(email)} is not str")
    else:
        email = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    if "address" in obj:
        address = obj["address"]
        address = _deserialize_separated_address_input(address)
    else:
        address = None
    if "zipcode" in obj:
        zipcode = obj["zipcode"]
        if not isinstance(zipcode, str):
            raise ValueError(f"{repr(zipcode)} is not str")
    else:
        zipcode = None
    if "businessRegistrationNumber" in obj:
        business_registration_number = obj["businessRegistrationNumber"]
        if not isinstance(business_registration_number, str):
            raise ValueError(f"{repr(business_registration_number)} is not str")
    else:
        business_registration_number = None
    return CustomerInput(id, name, birth_year, birth_month, birth_day, country, gender, email, phone_number, address, zipcode, business_registration_number)
