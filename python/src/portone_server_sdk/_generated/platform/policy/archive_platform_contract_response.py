from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract

@dataclass
class ArchivePlatformContractResponse:
    """계약 보관 성공 응답
    """
    contract: PlatformContract
    """보관된 계약
    """


def _serialize_archive_platform_contract_response(obj: ArchivePlatformContractResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["contract"] = _serialize_platform_contract(obj.contract)
    return entity


def _deserialize_archive_platform_contract_response(obj: Any) -> ArchivePlatformContractResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "contract" not in obj:
        raise KeyError(f"'contract' is not in {obj}")
    contract = obj["contract"]
    contract = _deserialize_platform_contract(contract)
    return ArchivePlatformContractResponse(contract)
