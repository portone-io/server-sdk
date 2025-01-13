from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.company.platform_business_status import PlatformBusinessStatus, _deserialize_platform_business_status, _serialize_platform_business_status
from ...platform.company.platform_taxation_type import PlatformTaxationType, _deserialize_platform_taxation_type, _serialize_platform_taxation_type

@dataclass
class PlatformCompanyState:
    taxation_type: PlatformTaxationType
    business_status: PlatformBusinessStatus
    taxation_type_date: Optional[str] = field(default=None)
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    closed_suspended_date: Optional[str] = field(default=None)
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """


def _serialize_platform_company_state(obj: PlatformCompanyState) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxationType"] = _serialize_platform_taxation_type(obj.taxation_type)
    entity["businessStatus"] = _serialize_platform_business_status(obj.business_status)
    if obj.taxation_type_date is not None:
        entity["taxationTypeDate"] = obj.taxation_type_date
    if obj.closed_suspended_date is not None:
        entity["closedSuspendedDate"] = obj.closed_suspended_date
    return entity


def _deserialize_platform_company_state(obj: Any) -> PlatformCompanyState:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxationType" not in obj:
        raise KeyError(f"'taxationType' is not in {obj}")
    taxation_type = obj["taxationType"]
    taxation_type = _deserialize_platform_taxation_type(taxation_type)
    if "businessStatus" not in obj:
        raise KeyError(f"'businessStatus' is not in {obj}")
    business_status = obj["businessStatus"]
    business_status = _deserialize_platform_business_status(business_status)
    if "taxationTypeDate" in obj:
        taxation_type_date = obj["taxationTypeDate"]
        if not isinstance(taxation_type_date, str):
            raise ValueError(f"{repr(taxation_type_date)} is not str")
    else:
        taxation_type_date = None
    if "closedSuspendedDate" in obj:
        closed_suspended_date = obj["closedSuspendedDate"]
        if not isinstance(closed_suspended_date, str):
            raise ValueError(f"{repr(closed_suspended_date)} is not str")
    else:
        closed_suspended_date = None
    return PlatformCompanyState(taxation_type, business_status, taxation_type_date, closed_suspended_date)
