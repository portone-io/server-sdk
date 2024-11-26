from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerContractSummary:
    """파트너 계약 요약 정보
    """
    id: str
    """계약 고유 아이디
    """
    name: str
    """계약 이름
    """


def _serialize_platform_partner_contract_summary(obj: PlatformPartnerContractSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["name"] = obj.name
    return entity


def _deserialize_platform_partner_contract_summary(obj: Any) -> PlatformPartnerContractSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    return PlatformPartnerContractSummary(id, name)
