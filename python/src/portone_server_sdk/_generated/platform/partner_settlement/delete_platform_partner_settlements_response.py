from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeletePlatformPartnerSettlementsResponse:
    """정산내역 삭제 결과
    """
    pass


def _serialize_delete_platform_partner_settlements_response(obj: DeletePlatformPartnerSettlementsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_delete_platform_partner_settlements_response(obj: Any) -> DeletePlatformPartnerSettlementsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return DeletePlatformPartnerSettlementsResponse()
