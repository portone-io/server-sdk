from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPartnerBusinessStatus = Literal["NOT_VERIFIED", "VERIFY_FAILED", "NOT_FOUND", "VERIFYING", "IN_BUSINESS", "CLOSED", "SUSPENDED"]
"""플랫폼 파트너 사업자 상태
"""


def _serialize_platform_partner_business_status(obj: PlatformPartnerBusinessStatus) -> Any:
    return obj


def _deserialize_platform_partner_business_status(obj: Any) -> PlatformPartnerBusinessStatus:
    if obj not in ["NOT_VERIFIED", "VERIFY_FAILED", "NOT_FOUND", "VERIFYING", "IN_BUSINESS", "CLOSED", "SUSPENDED"]:
        raise ValueError(f"{repr(obj)} is not PlatformPartnerBusinessStatus")
    return obj
