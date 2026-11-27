from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_manual_transfer import PlatformManualTransfer, _deserialize_platform_manual_transfer, _serialize_platform_manual_transfer

@dataclass
class CreateManualTransferResponse:
    transfer: PlatformManualTransfer


def _serialize_create_manual_transfer_response(obj: CreateManualTransferResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["transfer"] = _serialize_platform_manual_transfer(obj.transfer)
    return entity


def _deserialize_create_manual_transfer_response(obj: Any) -> CreateManualTransferResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "transfer" not in obj:
        raise KeyError("Missing required field 'transfer'")
    transfer = obj["transfer"]
    transfer = _deserialize_platform_manual_transfer(transfer)
    return CreateManualTransferResponse(transfer)
