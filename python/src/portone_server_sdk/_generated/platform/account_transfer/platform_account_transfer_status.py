from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformAccountTransferStatus = Union[Literal["PREPARED", "SCHEDULED", "CANCELLED", "STOPPED", "PROCESSING", "ASYNC_PROCESSING", "SUCCEEDED", "FAILED"], str]
"""계좌 이체 상태
"""


def _serialize_platform_account_transfer_status(obj: PlatformAccountTransferStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_account_transfer_status(obj: Any) -> PlatformAccountTransferStatus:
    return obj
