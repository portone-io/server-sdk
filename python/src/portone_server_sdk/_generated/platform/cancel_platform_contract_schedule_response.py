from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelPlatformContractScheduleResponse:
    """계약 예약 업데이트 취소 성공 응답
    """
    pass


def _serialize_cancel_platform_contract_schedule_response(obj: CancelPlatformContractScheduleResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_cancel_platform_contract_schedule_response(obj: Any) -> CancelPlatformContractScheduleResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return CancelPlatformContractScheduleResponse()
