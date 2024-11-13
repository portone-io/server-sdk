from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPartnerBusinessStatus = Union[Literal["NOT_VERIFIED", "VERIFY_ERROR", "NOT_FOUND", "IN_BUSINESS", "CLOSED", "SUSPENDED"], str]
"""플랫폼 파트너 사업자 상태
"""


def _serialize_platform_partner_business_status(obj: PlatformPartnerBusinessStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_partner_business_status(obj: Any) -> PlatformPartnerBusinessStatus:
    return obj
