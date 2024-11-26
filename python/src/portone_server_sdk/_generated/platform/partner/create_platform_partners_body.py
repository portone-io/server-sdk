from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.partner.create_platform_partner_body import CreatePlatformPartnerBody, _deserialize_create_platform_partner_body, _serialize_create_platform_partner_body

@dataclass
class CreatePlatformPartnersBody:
    """파트너 다건 생성을 위한 입력 정보
    """
    partners: list[CreatePlatformPartnerBody]
    """생성할 파트너 리스트 정보
    """


def _serialize_create_platform_partners_body(obj: CreatePlatformPartnersBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partners"] = list(map(_serialize_create_platform_partner_body, obj.partners))
    return entity


def _deserialize_create_platform_partners_body(obj: Any) -> CreatePlatformPartnersBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partners" not in obj:
        raise KeyError(f"'partners' is not in {obj}")
    partners = obj["partners"]
    if not isinstance(partners, list):
        raise ValueError(f"{repr(partners)} is not list")
    for i, item in enumerate(partners):
        item = _deserialize_create_platform_partner_body(item)
        partners[i] = item
    return CreatePlatformPartnersBody(partners)
