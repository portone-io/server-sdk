from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.platform_manual_transfer import PlatformManualTransfer, _deserialize_platform_manual_transfer, _serialize_platform_manual_transfer

@dataclass
class CreateManualTransferResponse:
    transfer: PlatformManualTransfer


def _serialize_create_manual_transfer_response(obj: CreateManualTransferResponse) -> Any:
    entity = {}
    entity["transfer"] = _serialize_platform_manual_transfer(obj.transfer)
    return entity


def _deserialize_create_manual_transfer_response(obj: Any) -> CreateManualTransferResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "transfer" not in obj:
        raise KeyError(f"'transfer' is not in {obj}")
    transfer = obj["transfer"]
    transfer = _deserialize_platform_manual_transfer(transfer)
    return CreateManualTransferResponse(transfer)
