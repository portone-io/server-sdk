from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.member_company.b2b_company_contact_input import B2bCompanyContactInput, _deserialize_b2b_company_contact_input, _serialize_b2b_company_contact_input
from portone_server_sdk._generated.b2b.member_company.b2b_member_company_input import B2bMemberCompanyInput, _deserialize_b2b_member_company_input, _serialize_b2b_member_company_input

@dataclass
class RegisterB2bMemberCompanyBody:
    """사업자 연동 요청 정보
    """
    company: B2bMemberCompanyInput
    """사업자 정보
    """
    contact: B2bCompanyContactInput
    """담당자 정보
    """


def _serialize_register_b2b_member_company_body(obj: RegisterB2bMemberCompanyBody) -> Any:
    entity = {}
    entity["company"] = _serialize_b2b_member_company_input(obj.company)
    entity["contact"] = _serialize_b2b_company_contact_input(obj.contact)
    return entity


def _deserialize_register_b2b_member_company_body(obj: Any) -> RegisterB2bMemberCompanyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "company" not in obj:
        raise KeyError(f"'company' is not in {obj}")
    company = obj["company"]
    company = _deserialize_b2b_member_company_input(company)
    if "contact" not in obj:
        raise KeyError(f"'contact' is not in {obj}")
    contact = obj["contact"]
    contact = _deserialize_b2b_company_contact_input(contact)
    return RegisterB2bMemberCompanyBody(company, contact)
