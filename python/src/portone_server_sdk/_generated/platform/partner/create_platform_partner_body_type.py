from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.partner.create_platform_partner_body_type_business import CreatePlatformPartnerBodyTypeBusiness, _deserialize_create_platform_partner_body_type_business, _serialize_create_platform_partner_body_type_business
from ...platform.partner.create_platform_partner_body_type_non_wht_payer import CreatePlatformPartnerBodyTypeNonWhtPayer, _deserialize_create_platform_partner_body_type_non_wht_payer, _serialize_create_platform_partner_body_type_non_wht_payer
from ...platform.partner.create_platform_partner_body_type_wht_payer import CreatePlatformPartnerBodyTypeWhtPayer, _deserialize_create_platform_partner_body_type_wht_payer, _serialize_create_platform_partner_body_type_wht_payer

@dataclass
class CreatePlatformPartnerBodyType:
    """파트너 생성을 위한 유형별 추가 정보
    """
    business: Optional[CreatePlatformPartnerBodyTypeBusiness] = field(default=None)
    """사업자 추가 정보
    """
    wht_payer: Optional[CreatePlatformPartnerBodyTypeWhtPayer] = field(default=None)
    """원천징수 대상자 추가 정보
    """
    non_wht_payer: Optional[CreatePlatformPartnerBodyTypeNonWhtPayer] = field(default=None)
    """원천징수 비대상자 추가 정보
    """


def _serialize_create_platform_partner_body_type(obj: CreatePlatformPartnerBodyType) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.business is not None:
        entity["business"] = _serialize_create_platform_partner_body_type_business(obj.business)
    if obj.wht_payer is not None:
        entity["whtPayer"] = _serialize_create_platform_partner_body_type_wht_payer(obj.wht_payer)
    if obj.non_wht_payer is not None:
        entity["nonWhtPayer"] = _serialize_create_platform_partner_body_type_non_wht_payer(obj.non_wht_payer)
    return entity


def _deserialize_create_platform_partner_body_type(obj: Any) -> CreatePlatformPartnerBodyType:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "business" in obj:
        business = obj["business"]
        business = _deserialize_create_platform_partner_body_type_business(business)
    else:
        business = None
    if "whtPayer" in obj:
        wht_payer = obj["whtPayer"]
        wht_payer = _deserialize_create_platform_partner_body_type_wht_payer(wht_payer)
    else:
        wht_payer = None
    if "nonWhtPayer" in obj:
        non_wht_payer = obj["nonWhtPayer"]
        non_wht_payer = _deserialize_create_platform_partner_body_type_non_wht_payer(non_wht_payer)
    else:
        non_wht_payer = None
    return CreatePlatformPartnerBodyType(business, wht_payer, non_wht_payer)
