from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.member_company.b2b_member_company import B2bMemberCompany, _deserialize_b2b_member_company, _serialize_b2b_member_company

@dataclass
class UpdateB2bMemberCompanyResponse:
    """연동 사업자 정보 수정 응답
    """
    member_company: B2bMemberCompany
    """연동 사업자 정보
    """


def _serialize_update_b2b_member_company_response(obj: UpdateB2bMemberCompanyResponse) -> Any:
    entity = {}
    entity["memberCompany"] = _serialize_b2b_member_company(obj.member_company)
    return entity


def _deserialize_update_b2b_member_company_response(obj: Any) -> UpdateB2bMemberCompanyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "memberCompany" not in obj:
        raise KeyError(f"'memberCompany' is not in {obj}")
    member_company = obj["memberCompany"]
    member_company = _deserialize_b2b_member_company(member_company)
    return UpdateB2bMemberCompanyResponse(member_company)
