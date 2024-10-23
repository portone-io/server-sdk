from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.b2b_company_contact import B2bCompanyContact, _deserialize_b2b_company_contact, _serialize_b2b_company_contact
from portone_server_sdk._generated.b2b.member_company.b2b_member_company import B2bMemberCompany, _deserialize_b2b_member_company, _serialize_b2b_member_company

@dataclass
class RegisterB2bMemberCompanyResponse:
    """사업자 연동 응답 정보
    """
    company: B2bMemberCompany
    """사업자 정보
    """
    contact: B2bCompanyContact
    """담당자 정보
    """


def _serialize_register_b2b_member_company_response(obj: RegisterB2bMemberCompanyResponse) -> Any:
    entity = {}
    entity["company"] = _serialize_b2b_member_company(obj.company)
    entity["contact"] = _serialize_b2b_company_contact(obj.contact)
    return entity


def _deserialize_register_b2b_member_company_response(obj: Any) -> RegisterB2bMemberCompanyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "company" not in obj:
        raise KeyError(f"'company' is not in {obj}")
    company = obj["company"]
    company = _deserialize_b2b_member_company(company)
    if "contact" not in obj:
        raise KeyError(f"'contact' is not in {obj}")
    contact = obj["contact"]
    contact = _deserialize_b2b_company_contact(contact)
    return RegisterB2bMemberCompanyResponse(company, contact)
