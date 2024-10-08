from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bMemberCompany:
    brn: str
    """사업자등록번호

    `-` 없이 숫자로만 구성됩니다.
    """
    name: str
    """회사명
    """
    ceo_name: str
    """대표자 성명
    """
    address: str
    """회사 주소
    """
    business_type: str
    """업태
    """
    business_class: str
    """업종
    """


def _serialize_b2b_member_company(obj: B2bMemberCompany) -> Any:
    entity = {}
    entity["brn"] = obj.brn
    entity["name"] = obj.name
    entity["ceoName"] = obj.ceo_name
    entity["address"] = obj.address
    entity["businessType"] = obj.business_type
    entity["businessClass"] = obj.business_class
    return entity


def _deserialize_b2b_member_company(obj: Any) -> B2bMemberCompany:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "ceoName" not in obj:
        raise KeyError(f"'ceoName' is not in {obj}")
    ceo_name = obj["ceoName"]
    if not isinstance(ceo_name, str):
        raise ValueError(f"{repr(ceo_name)} is not str")
    if "address" not in obj:
        raise KeyError(f"'address' is not in {obj}")
    address = obj["address"]
    if not isinstance(address, str):
        raise ValueError(f"{repr(address)} is not str")
    if "businessType" not in obj:
        raise KeyError(f"'businessType' is not in {obj}")
    business_type = obj["businessType"]
    if not isinstance(business_type, str):
        raise ValueError(f"{repr(business_type)} is not str")
    if "businessClass" not in obj:
        raise KeyError(f"'businessClass' is not in {obj}")
    business_class = obj["businessClass"]
    if not isinstance(business_class, str):
        raise ValueError(f"{repr(business_class)} is not str")
    return B2bMemberCompany(brn, name, ceo_name, address, business_type, business_class)
