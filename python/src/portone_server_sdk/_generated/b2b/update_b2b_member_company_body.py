from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class UpdateB2bMemberCompanyBody:
    """연동 사업자 정보 수정 요청
    """
    name: Optional[str]
    """회사명
    """
    ceo_name: Optional[str]
    """대표자 성명
    """
    address: Optional[str]
    """회사 주소
    """
    business_type: Optional[str]
    """업태
    """
    business_class: Optional[str]
    """업종
    """


def _serialize_update_b2b_member_company_body(obj: UpdateB2bMemberCompanyBody) -> Any:
    entity = {}
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.ceo_name is not None:
        entity["ceoName"] = obj.ceo_name
    if obj.address is not None:
        entity["address"] = obj.address
    if obj.business_type is not None:
        entity["businessType"] = obj.business_type
    if obj.business_class is not None:
        entity["businessClass"] = obj.business_class
    return entity


def _deserialize_update_b2b_member_company_body(obj: Any) -> UpdateB2bMemberCompanyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "ceoName" in obj:
        ceo_name = obj["ceoName"]
        if not isinstance(ceo_name, str):
            raise ValueError(f"{repr(ceo_name)} is not str")
    else:
        ceo_name = None
    if "address" in obj:
        address = obj["address"]
        if not isinstance(address, str):
            raise ValueError(f"{repr(address)} is not str")
    else:
        address = None
    if "businessType" in obj:
        business_type = obj["businessType"]
        if not isinstance(business_type, str):
            raise ValueError(f"{repr(business_type)} is not str")
    else:
        business_type = None
    if "businessClass" in obj:
        business_class = obj["businessClass"]
        if not isinstance(business_class, str):
            raise ValueError(f"{repr(business_class)} is not str")
    else:
        business_class = None
    return UpdateB2bMemberCompanyBody(name, ceo_name, address, business_type, business_class)
