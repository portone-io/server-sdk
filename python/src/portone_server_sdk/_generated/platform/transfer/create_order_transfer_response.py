from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_order_transfer import PlatformOrderTransfer, _deserialize_platform_order_transfer, _serialize_platform_order_transfer

@dataclass
class CreateOrderTransferResponse:
    transfer: PlatformOrderTransfer


def _serialize_create_order_transfer_response(obj: CreateOrderTransferResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["transfer"] = _serialize_platform_order_transfer(obj.transfer)
    return entity


def _deserialize_create_order_transfer_response(obj: Any) -> CreateOrderTransferResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "transfer" not in obj:
        raise KeyError("Missing required field 'transfer'")
    transfer = obj["transfer"]
    transfer = _deserialize_platform_order_transfer(transfer)
    return CreateOrderTransferResponse(transfer)
