from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract

@dataclass
class ReschedulePlatformContractResponse:
    """계약 예약 업데이트 재설정 성공 응답
    """
    scheduled_contract: PlatformContract
    """예약된 계약 정보
    """


def _serialize_reschedule_platform_contract_response(obj: ReschedulePlatformContractResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["scheduledContract"] = _serialize_platform_contract(obj.scheduled_contract)
    return entity


def _deserialize_reschedule_platform_contract_response(obj: Any) -> ReschedulePlatformContractResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "scheduledContract" not in obj:
        raise KeyError(f"'scheduledContract' is not in {obj}")
    scheduled_contract = obj["scheduledContract"]
    scheduled_contract = _deserialize_platform_contract(scheduled_contract)
    return ReschedulePlatformContractResponse(scheduled_contract)
