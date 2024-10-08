from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.platform_order_transfer import PlatformOrderTransfer, _deserialize_platform_order_transfer, _serialize_platform_order_transfer

@dataclass
class CreateOrderTransferResponse:
    transfer: PlatformOrderTransfer


def _serialize_create_order_transfer_response(obj: CreateOrderTransferResponse) -> Any:
    entity = {}
    entity["transfer"] = _serialize_platform_order_transfer(obj.transfer)
    return entity


def _deserialize_create_order_transfer_response(obj: Any) -> CreateOrderTransferResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "transfer" not in obj:
        raise KeyError(f"'transfer' is not in {obj}")
    transfer = obj["transfer"]
    transfer = _deserialize_platform_order_transfer(transfer)
    return CreateOrderTransferResponse(transfer)
