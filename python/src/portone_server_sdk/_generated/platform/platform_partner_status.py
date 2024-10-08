from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPartnerStatus = Literal["PENDING", "APPROVED", "REJECTED"]
"""플랫폼 파트너 상태
"""


def _serialize_platform_partner_status(obj: PlatformPartnerStatus) -> Any:
    return obj


def _deserialize_platform_partner_status(obj: Any) -> PlatformPartnerStatus:
    if obj not in ["PENDING", "APPROVED", "REJECTED"]:
        raise ValueError(f"{repr(obj)} is not PlatformPartnerStatus")
    return obj
