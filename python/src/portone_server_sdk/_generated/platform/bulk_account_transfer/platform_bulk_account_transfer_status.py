from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformBulkAccountTransferStatus = Union[Literal["PREPARED", "SCHEDULED", "ONGOING", "COMPLETED"], str]


def _serialize_platform_bulk_account_transfer_status(obj: PlatformBulkAccountTransferStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_bulk_account_transfer_status(obj: Any) -> PlatformBulkAccountTransferStatus:
    return obj
