from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract

@dataclass
class RecoverPlatformContractResponse:
    """계약 복원 성공 응답
    """
    contract: PlatformContract
    """복원된 계약
    """


def _serialize_recover_platform_contract_response(obj: RecoverPlatformContractResponse) -> Any:
    entity = {}
    entity["contract"] = _serialize_platform_contract(obj.contract)
    return entity


def _deserialize_recover_platform_contract_response(obj: Any) -> RecoverPlatformContractResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "contract" not in obj:
        raise KeyError(f"'contract' is not in {obj}")
    contract = obj["contract"]
    contract = _deserialize_platform_contract(contract)
    return RecoverPlatformContractResponse(contract)
