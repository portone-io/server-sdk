from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update_type_business import SchedulePlatformPartnersBodyUpdateTypeBusiness, _deserialize_schedule_platform_partners_body_update_type_business, _serialize_schedule_platform_partners_body_update_type_business
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update_type_non_wht_payer import SchedulePlatformPartnersBodyUpdateTypeNonWhtPayer, _deserialize_schedule_platform_partners_body_update_type_non_wht_payer, _serialize_schedule_platform_partners_body_update_type_non_wht_payer
from portone_server_sdk._generated.platform.schedule_platform_partners_body_update_type_wht_payer import SchedulePlatformPartnersBodyUpdateTypeWhtPayer, _deserialize_schedule_platform_partners_body_update_type_wht_payer, _serialize_schedule_platform_partners_body_update_type_wht_payer

@dataclass
class SchedulePlatformPartnersBodyUpdateType:
    """파트너 유형별 정보 업데이트를 위한 입력 정보

    파트너 유형별 추가 정보를 수정합니다.
    최초 생성된 유형 내에서 세부 정보만 수정할 수 있고 파트너의 유형 자체를 수정할 수는 없습니다.
    """
    business: Optional[SchedulePlatformPartnersBodyUpdateTypeBusiness]
    """사업자 추가 정보
    """
    wht_payer: Optional[SchedulePlatformPartnersBodyUpdateTypeWhtPayer]
    """원천징수 대상자 추가 정보
    """
    non_wht_payer: Optional[SchedulePlatformPartnersBodyUpdateTypeNonWhtPayer]
    """원천징수 비대상자 추가 정보
    """


def _serialize_schedule_platform_partners_body_update_type(obj: SchedulePlatformPartnersBodyUpdateType) -> Any:
    entity = {}
    if obj.business is not None:
        entity["business"] = _serialize_schedule_platform_partners_body_update_type_business(obj.business)
    if obj.wht_payer is not None:
        entity["whtPayer"] = _serialize_schedule_platform_partners_body_update_type_wht_payer(obj.wht_payer)
    if obj.non_wht_payer is not None:
        entity["nonWhtPayer"] = _serialize_schedule_platform_partners_body_update_type_non_wht_payer(obj.non_wht_payer)
    return entity


def _deserialize_schedule_platform_partners_body_update_type(obj: Any) -> SchedulePlatformPartnersBodyUpdateType:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "business" in obj:
        business = obj["business"]
        business = _deserialize_schedule_platform_partners_body_update_type_business(business)
    else:
        business = None
    if "whtPayer" in obj:
        wht_payer = obj["whtPayer"]
        wht_payer = _deserialize_schedule_platform_partners_body_update_type_wht_payer(wht_payer)
    else:
        wht_payer = None
    if "nonWhtPayer" in obj:
        non_wht_payer = obj["nonWhtPayer"]
        non_wht_payer = _deserialize_schedule_platform_partners_body_update_type_non_wht_payer(non_wht_payer)
    else:
        non_wht_payer = None
    return SchedulePlatformPartnersBodyUpdateType(business, wht_payer, non_wht_payer)
