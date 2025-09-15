from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformBulkTaskType = Union[Literal["CREATE_TRANSFERS", "CREATE_PARTNERS", "CONNECT_MEMBER_COMPANIES", "DISCONNECT_MEMBER_COMPANIES", "SEND_PAYOUT_SETTLEMENT_STATEMENTS"], str]


def _serialize_platform_bulk_task_type(obj: PlatformBulkTaskType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_bulk_task_type(obj: Any) -> PlatformBulkTaskType:
    return obj
