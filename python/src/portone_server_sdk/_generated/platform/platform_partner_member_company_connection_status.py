from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPartnerMemberCompanyConnectionStatus = Union[Literal["NOT_CONNECTED", "CONNECT_PENDING", "CONNECTED", "CONNECT_FAILED", "DISCONNECT_PENDING"], str]
"""플랫폼 파트너 연동 사업자 연결 상태
"""


def _serialize_platform_partner_member_company_connection_status(obj: PlatformPartnerMemberCompanyConnectionStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_partner_member_company_connection_status(obj: Any) -> PlatformPartnerMemberCompanyConnectionStatus:
    return obj
