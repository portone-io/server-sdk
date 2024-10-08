from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from portone_server_sdk._generated.platform.platform_additional_fee_policy import PlatformAdditionalFeePolicy, _deserialize_platform_additional_fee_policy, _serialize_platform_additional_fee_policy

@dataclass
class GetPlatformAdditionalFeePoliciesResponse:
    """추가 수수료 정책 다건 조회 성공 응답 정보
    """
    items: list[PlatformAdditionalFeePolicy]
    """조회된 추가 수수료 정책 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_platform_additional_fee_policies_response(obj: GetPlatformAdditionalFeePoliciesResponse) -> Any:
    entity = {}
    entity["items"] = list(map(_serialize_platform_additional_fee_policy, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_platform_additional_fee_policies_response(obj: Any) -> GetPlatformAdditionalFeePoliciesResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_platform_additional_fee_policy(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetPlatformAdditionalFeePoliciesResponse(items, page)
