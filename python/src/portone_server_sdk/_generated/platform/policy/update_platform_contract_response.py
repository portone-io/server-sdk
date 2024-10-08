from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract

@dataclass
class UpdatePlatformContractResponse:
    """계약 객체 업데이트 성공 응답
    """
    contract: PlatformContract
    """업데이트된 계약 객체
    """


def _serialize_update_platform_contract_response(obj: UpdatePlatformContractResponse) -> Any:
    entity = {}
    entity["contract"] = _serialize_platform_contract(obj.contract)
    return entity


def _deserialize_update_platform_contract_response(obj: Any) -> UpdatePlatformContractResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "contract" not in obj:
        raise KeyError(f"'contract' is not in {obj}")
    contract = obj["contract"]
    contract = _deserialize_platform_contract(contract)
    return UpdatePlatformContractResponse(contract)
