from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreatePlatformOrderCancelTransferBodyOrderDetailAll:
    """전체 금액 취소
    """
    pass


def _serialize_create_platform_order_cancel_transfer_body_order_detail_all(obj: CreatePlatformOrderCancelTransferBodyOrderDetailAll) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_create_platform_order_cancel_transfer_body_order_detail_all(obj: Any) -> CreatePlatformOrderCancelTransferBodyOrderDetailAll:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return CreatePlatformOrderCancelTransferBodyOrderDetailAll()
