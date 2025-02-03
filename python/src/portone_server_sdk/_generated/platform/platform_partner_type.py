from __future__ import annotations
from typing import Any, Optional, Union
from ..platform.platform_partner_type_business import PlatformPartnerTypeBusiness, _deserialize_platform_partner_type_business, _serialize_platform_partner_type_business
from ..platform.platform_partner_type_non_wht_payer import PlatformPartnerTypeNonWhtPayer, _deserialize_platform_partner_type_non_wht_payer, _serialize_platform_partner_type_non_wht_payer
from ..platform.platform_partner_type_wht_payer import PlatformPartnerTypeWhtPayer, _deserialize_platform_partner_type_wht_payer, _serialize_platform_partner_type_wht_payer

PlatformPartnerType = Union[PlatformPartnerTypeBusiness, PlatformPartnerTypeNonWhtPayer, PlatformPartnerTypeWhtPayer, dict]
"""파트너 유형별 추가 정보
"""


def _serialize_platform_partner_type(obj: PlatformPartnerType) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformPartnerTypeBusiness):
        return _serialize_platform_partner_type_business(obj)
    if isinstance(obj, PlatformPartnerTypeNonWhtPayer):
        return _serialize_platform_partner_type_non_wht_payer(obj)
    if isinstance(obj, PlatformPartnerTypeWhtPayer):
        return _serialize_platform_partner_type_wht_payer(obj)


def _deserialize_platform_partner_type(obj: Any) -> PlatformPartnerType:
    try:
        return _deserialize_platform_partner_type_business(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_type_non_wht_payer(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_type_wht_payer(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformPartnerType")
