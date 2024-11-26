from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPartnerStatus = Union[Literal["PENDING", "APPROVED", "REJECTED"], str]
"""플랫폼 파트너 상태
"""


def _serialize_platform_partner_status(obj: PlatformPartnerStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_partner_status(obj: Any) -> PlatformPartnerStatus:
    return obj
