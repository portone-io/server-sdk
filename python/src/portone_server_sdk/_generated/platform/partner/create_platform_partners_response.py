from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class CreatePlatformPartnersResponse:
    """파트너 다건 생성 성공 응답
    """
    partners: list[PlatformPartner]
    """생성된 파트너 리스트
    """


def _serialize_create_platform_partners_response(obj: CreatePlatformPartnersResponse) -> Any:
    entity = {}
    entity["partners"] = list(map(_serialize_platform_partner, obj.partners))
    return entity


def _deserialize_create_platform_partners_response(obj: Any) -> CreatePlatformPartnersResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partners" not in obj:
        raise KeyError(f"'partners' is not in {obj}")
    partners = obj["partners"]
    if not isinstance(partners, list):
        raise ValueError(f"{repr(partners)} is not list")
    for i, item in enumerate(partners):
        item = _deserialize_platform_partner(item)
        partners[i] = item
    return CreatePlatformPartnersResponse(partners)
