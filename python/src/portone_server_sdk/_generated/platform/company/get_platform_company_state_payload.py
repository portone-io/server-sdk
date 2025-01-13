from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.company.platform_company_state import PlatformCompanyState, _deserialize_platform_company_state, _serialize_platform_company_state

@dataclass
class GetPlatformCompanyStatePayload:
    """사업자 조회 성공 응답 정보
    """
    company_state: PlatformCompanyState
    """사업자 정보
    """
    company_verification_id: str
    """사업자 검증 아이디
    """


def _serialize_get_platform_company_state_payload(obj: GetPlatformCompanyStatePayload) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["companyState"] = _serialize_platform_company_state(obj.company_state)
    entity["companyVerificationId"] = obj.company_verification_id
    return entity


def _deserialize_get_platform_company_state_payload(obj: Any) -> GetPlatformCompanyStatePayload:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "companyState" not in obj:
        raise KeyError(f"'companyState' is not in {obj}")
    company_state = obj["companyState"]
    company_state = _deserialize_platform_company_state(company_state)
    if "companyVerificationId" not in obj:
        raise KeyError(f"'companyVerificationId' is not in {obj}")
    company_verification_id = obj["companyVerificationId"]
    if not isinstance(company_verification_id, str):
        raise ValueError(f"{repr(company_verification_id)} is not str")
    return GetPlatformCompanyStatePayload(company_state, company_verification_id)
