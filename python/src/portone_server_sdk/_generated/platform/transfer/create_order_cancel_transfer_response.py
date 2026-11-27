from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_order_cancel_transfer import PlatformOrderCancelTransfer, _deserialize_platform_order_cancel_transfer, _serialize_platform_order_cancel_transfer

@dataclass
class CreateOrderCancelTransferResponse:
    transfer: PlatformOrderCancelTransfer


def _serialize_create_order_cancel_transfer_response(obj: CreateOrderCancelTransferResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["transfer"] = _serialize_platform_order_cancel_transfer(obj.transfer)
    return entity


def _deserialize_create_order_cancel_transfer_response(obj: Any) -> CreateOrderCancelTransferResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "transfer" not in obj:
        raise KeyError("Missing required field 'transfer'")
    transfer = obj["transfer"]
    transfer = _deserialize_platform_order_cancel_transfer(transfer)
    return CreateOrderCancelTransferResponse(transfer)
