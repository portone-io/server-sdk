from __future__ import annotations
from typing import Any, Literal, Optional

PlatformTransferType = Literal["ORDER", "ORDER_CANCEL", "MANUAL"]


def _serialize_platform_transfer_type(obj: PlatformTransferType) -> Any:
    return obj


def _deserialize_platform_transfer_type(obj: Any) -> PlatformTransferType:
    if obj not in ["ORDER", "ORDER_CANCEL", "MANUAL"]:
        raise ValueError(f"{repr(obj)} is not PlatformTransferType")
    return obj
