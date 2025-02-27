from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformBulkTaskStatus = Union[Literal["PREPARED", "PROCESSING", "COMPLETED", "CANCELED"], str]


def _serialize_platform_bulk_task_status(obj: PlatformBulkTaskStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_bulk_task_status(obj: Any) -> PlatformBulkTaskStatus:
    return obj
