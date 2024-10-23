from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bMemberCompanyInput:
    """사업자 입력 정보
    """
    brn: str
    """사업자등록번호
    """
    company_name: str
    """회사명
    """
    representative_name: str
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


def _serialize_b2b_member_company_input(obj: B2bMemberCompanyInput) -> Any:
    entity = {}
    entity["brn"] = obj.brn
    entity["companyName"] = obj.company_name
    entity["representativeName"] = obj.representative_name
    entity["address"] = obj.address
    entity["businessType"] = obj.business_type
    entity["businessClass"] = obj.business_class
    return entity


def _deserialize_b2b_member_company_input(obj: Any) -> B2bMemberCompanyInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "companyName" not in obj:
        raise KeyError(f"'companyName' is not in {obj}")
    company_name = obj["companyName"]
    if not isinstance(company_name, str):
        raise ValueError(f"{repr(company_name)} is not str")
    if "representativeName" not in obj:
        raise KeyError(f"'representativeName' is not in {obj}")
    representative_name = obj["representativeName"]
    if not isinstance(representative_name, str):
        raise ValueError(f"{repr(representative_name)} is not str")
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
    return B2bMemberCompanyInput(brn, company_name, representative_name, address, business_type, business_class)
