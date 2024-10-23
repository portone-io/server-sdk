from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.b2b_company_state_business_status import B2bCompanyStateBusinessStatus, _deserialize_b2b_company_state_business_status, _serialize_b2b_company_state_business_status
from portone_server_sdk._generated.b2b.member_company.b2b_company_state_taxation_type import B2bCompanyStateTaxationType, _deserialize_b2b_company_state_taxation_type, _serialize_b2b_company_state_taxation_type

@dataclass
class B2bCompanyState:
    """사업자 상태
    """
    taxation_type: B2bCompanyStateTaxationType
    """사업자 과세 유형
    """
    business_status: B2bCompanyStateBusinessStatus
    """사업자 영업 상태
    """
    taxation_type_update_date: Optional[str]
    """과세 유형 변경 일자

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    closed_suspended_date: Optional[str]
    """휴폐업 일자

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """


def _serialize_b2b_company_state(obj: B2bCompanyState) -> Any:
    entity = {}
    entity["taxationType"] = _serialize_b2b_company_state_taxation_type(obj.taxation_type)
    entity["businessStatus"] = _serialize_b2b_company_state_business_status(obj.business_status)
    if obj.taxation_type_update_date is not None:
        entity["taxationTypeUpdateDate"] = obj.taxation_type_update_date
    if obj.closed_suspended_date is not None:
        entity["closedSuspendedDate"] = obj.closed_suspended_date
    return entity


def _deserialize_b2b_company_state(obj: Any) -> B2bCompanyState:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxationType" not in obj:
        raise KeyError(f"'taxationType' is not in {obj}")
    taxation_type = obj["taxationType"]
    taxation_type = _deserialize_b2b_company_state_taxation_type(taxation_type)
    if "businessStatus" not in obj:
        raise KeyError(f"'businessStatus' is not in {obj}")
    business_status = obj["businessStatus"]
    business_status = _deserialize_b2b_company_state_business_status(business_status)
    if "taxationTypeUpdateDate" in obj:
        taxation_type_update_date = obj["taxationTypeUpdateDate"]
        if not isinstance(taxation_type_update_date, str):
            raise ValueError(f"{repr(taxation_type_update_date)} is not str")
    else:
        taxation_type_update_date = None
    if "closedSuspendedDate" in obj:
        closed_suspended_date = obj["closedSuspendedDate"]
        if not isinstance(closed_suspended_date, str):
            raise ValueError(f"{repr(closed_suspended_date)} is not str")
    else:
        closed_suspended_date = None
    return B2bCompanyState(taxation_type, business_status, taxation_type_update_date, closed_suspended_date)
