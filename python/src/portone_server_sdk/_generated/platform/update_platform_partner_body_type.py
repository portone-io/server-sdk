from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.update_platform_partner_body_type_business import UpdatePlatformPartnerBodyTypeBusiness, _deserialize_update_platform_partner_body_type_business, _serialize_update_platform_partner_body_type_business
from portone_server_sdk._generated.platform.update_platform_partner_body_type_non_wht_payer import UpdatePlatformPartnerBodyTypeNonWhtPayer, _deserialize_update_platform_partner_body_type_non_wht_payer, _serialize_update_platform_partner_body_type_non_wht_payer
from portone_server_sdk._generated.platform.update_platform_partner_body_type_wht_payer import UpdatePlatformPartnerBodyTypeWhtPayer, _deserialize_update_platform_partner_body_type_wht_payer, _serialize_update_platform_partner_body_type_wht_payer

@dataclass
class UpdatePlatformPartnerBodyType:
    """파트너 업데이트를 위한 유형별 추가 정보

    파트너 유형별 추가 정보를 수정합니다.
    기존과 다른 파트너 유형 정보가 입력된 경우, 파트너의 유형 자체가 변경됩니다.
    """
    business: Optional[UpdatePlatformPartnerBodyTypeBusiness]
    """사업자 추가 정보
    """
    wht_payer: Optional[UpdatePlatformPartnerBodyTypeWhtPayer]
    """원천징수 대상자 추가 정보
    """
    non_wht_payer: Optional[UpdatePlatformPartnerBodyTypeNonWhtPayer]
    """원천징수 비대상자 추가 정보
    """


def _serialize_update_platform_partner_body_type(obj: UpdatePlatformPartnerBodyType) -> Any:
    entity = {}
    if obj.business is not None:
        entity["business"] = _serialize_update_platform_partner_body_type_business(obj.business)
    if obj.wht_payer is not None:
        entity["whtPayer"] = _serialize_update_platform_partner_body_type_wht_payer(obj.wht_payer)
    if obj.non_wht_payer is not None:
        entity["nonWhtPayer"] = _serialize_update_platform_partner_body_type_non_wht_payer(obj.non_wht_payer)
    return entity


def _deserialize_update_platform_partner_body_type(obj: Any) -> UpdatePlatformPartnerBodyType:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "business" in obj:
        business = obj["business"]
        business = _deserialize_update_platform_partner_body_type_business(business)
    else:
        business = None
    if "whtPayer" in obj:
        wht_payer = obj["whtPayer"]
        wht_payer = _deserialize_update_platform_partner_body_type_wht_payer(wht_payer)
    else:
        wht_payer = None
    if "nonWhtPayer" in obj:
        non_wht_payer = obj["nonWhtPayer"]
        non_wht_payer = _deserialize_update_platform_partner_body_type_non_wht_payer(non_wht_payer)
    else:
        non_wht_payer = None
    return UpdatePlatformPartnerBodyType(business, wht_payer, non_wht_payer)
