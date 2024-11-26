from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract

@dataclass
class CreatePlatformContractResponse:
    """계약 객체 생성 성공 응답
    """
    contract: PlatformContract
    """생성된 계약 객체
    """


def _serialize_create_platform_contract_response(obj: CreatePlatformContractResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["contract"] = _serialize_platform_contract(obj.contract)
    return entity


def _deserialize_create_platform_contract_response(obj: Any) -> CreatePlatformContractResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "contract" not in obj:
        raise KeyError(f"'contract' is not in {obj}")
    contract = obj["contract"]
    contract = _deserialize_platform_contract(contract)
    return CreatePlatformContractResponse(contract)
