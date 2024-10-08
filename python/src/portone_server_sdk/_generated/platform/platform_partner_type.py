from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.platform.platform_partner_type_business import PlatformPartnerTypeBusiness, _deserialize_platform_partner_type_business, _serialize_platform_partner_type_business
from portone_server_sdk._generated.platform.platform_partner_type_non_wht_payer import PlatformPartnerTypeNonWhtPayer, _deserialize_platform_partner_type_non_wht_payer, _serialize_platform_partner_type_non_wht_payer
from portone_server_sdk._generated.platform.platform_partner_type_wht_payer import PlatformPartnerTypeWhtPayer, _deserialize_platform_partner_type_wht_payer, _serialize_platform_partner_type_wht_payer

PlatformPartnerType = Union[PlatformPartnerTypeBusiness, PlatformPartnerTypeNonWhtPayer, PlatformPartnerTypeWhtPayer]
"""파트너 유형별 추가 정보
"""


def _serialize_platform_partner_type(obj: PlatformPartnerType) -> Any:
    if obj.type == "BUSINESS":
        return _serialize_platform_partner_type_business(obj)
    if obj.type == "NON_WHT_PAYER":
        return _serialize_platform_partner_type_non_wht_payer(obj)
    if obj.type == "WHT_PAYER":
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
