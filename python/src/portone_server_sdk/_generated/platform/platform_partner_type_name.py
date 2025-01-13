from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPartnerTypeName = Union[Literal["BUSINESS", "WHT_PAYER", "NON_WHT_PAYER"], str]
"""플랫폼 파트너 유형 이름
"""


def _serialize_platform_partner_type_name(obj: PlatformPartnerTypeName) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_partner_type_name(obj: Any) -> PlatformPartnerTypeName:
    return obj
