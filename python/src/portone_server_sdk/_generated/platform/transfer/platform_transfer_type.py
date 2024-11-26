from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformTransferType = Union[Literal["ORDER", "ORDER_CANCEL", "MANUAL"], str]


def _serialize_platform_transfer_type(obj: PlatformTransferType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_transfer_type(obj: Any) -> PlatformTransferType:
    return obj
