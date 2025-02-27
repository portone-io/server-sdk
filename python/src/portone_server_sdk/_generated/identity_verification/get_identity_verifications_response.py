from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..identity_verification.identity_verification import IdentityVerification, _deserialize_identity_verification, _serialize_identity_verification
from ..common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info

@dataclass
class GetIdentityVerificationsResponse:
    """본인인증 내역 다건 조회 성공 응답 정보
    """
    items: list[IdentityVerification]
    """조회된 본인인증 내역 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_identity_verifications_response(obj: GetIdentityVerificationsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_identity_verification, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_identity_verifications_response(obj: Any) -> GetIdentityVerificationsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_identity_verification(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetIdentityVerificationsResponse(items, page)
