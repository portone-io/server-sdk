from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.address import Address, _deserialize_address, _serialize_address
from portone_server_sdk._generated.common.gender import Gender, _deserialize_gender, _serialize_gender

@dataclass
class Customer:
    """고객 정보
    """
    id: Optional[str]
    """고객 아이디

    고객사가 지정한 고객의 고유 식별자입니다.
    """
    name: Optional[str]
    """이름
    """
    birth_year: Optional[str]
    """출생 연도
    """
    gender: Optional[Gender]
    """성별
    """
    email: Optional[str]
    """이메일
    """
    phone_number: Optional[str]
    """전화번호
    """
    address: Optional[Address]
    """주소
    """
    zipcode: Optional[str]
    """우편번호
    """


def _serialize_customer(obj: Customer) -> Any:
    entity = {}
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.birth_year is not None:
        entity["birthYear"] = obj.birth_year
    if obj.gender is not None:
        entity["gender"] = _serialize_gender(obj.gender)
    if obj.email is not None:
        entity["email"] = obj.email
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.address is not None:
        entity["address"] = _serialize_address(obj.address)
    if obj.zipcode is not None:
        entity["zipcode"] = obj.zipcode
    return entity


def _deserialize_customer(obj: Any) -> Customer:
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
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "birthYear" in obj:
        birth_year = obj["birthYear"]
        if not isinstance(birth_year, str):
            raise ValueError(f"{repr(birth_year)} is not str")
    else:
        birth_year = None
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
        address = _deserialize_address(address)
    else:
        address = None
    if "zipcode" in obj:
        zipcode = obj["zipcode"]
        if not isinstance(zipcode, str):
            raise ValueError(f"{repr(zipcode)} is not str")
    else:
        zipcode = None
    return Customer(id, name, birth_year, gender, email, phone_number, address, zipcode)
