from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bMemberCompany:
    id: str
    """아이디(사업자등록번호)
    """
    graphql_id: str
    brn: str
    """사업자등록번호

    `-` 없이 숫자로만 구성됩니다.
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
    contact_id: str
    """담당자 ID
    """


def _serialize_b2b_member_company(obj: B2bMemberCompany) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["brn"] = obj.brn
    entity["companyName"] = obj.company_name
    entity["representativeName"] = obj.representative_name
    entity["address"] = obj.address
    entity["businessType"] = obj.business_type
    entity["businessClass"] = obj.business_class
    entity["contactId"] = obj.contact_id
    return entity


def _deserialize_b2b_member_company(obj: Any) -> B2bMemberCompany:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
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
    if "contactId" not in obj:
        raise KeyError(f"'contactId' is not in {obj}")
    contact_id = obj["contactId"]
    if not isinstance(contact_id, str):
        raise ValueError(f"{repr(contact_id)} is not str")
    return B2bMemberCompany(id, graphql_id, brn, company_name, representative_name, address, business_type, business_class, contact_id)
