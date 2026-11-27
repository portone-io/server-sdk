from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformTransferAlreadyExistsError:
    transfer_id: str
    transfer_graphql_id: str
    message: Optional[str] = field(default=None)


def _serialize_platform_transfer_already_exists_error(obj: PlatformTransferAlreadyExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_TRANSFER_ALREADY_EXISTS"
    entity["transferId"] = obj.transfer_id
    entity["transferGraphqlId"] = obj.transfer_graphql_id
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_transfer_already_exists_error(obj: Any) -> PlatformTransferAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_TRANSFER_ALREADY_EXISTS":
        raise ValueError("Expected 'PLATFORM_TRANSFER_ALREADY_EXISTS' for type")
    if "transferId" not in obj:
        raise KeyError("Missing required field 'transferId'")
    transfer_id = obj["transferId"]
    if not isinstance(transfer_id, str):
        raise ValueError("Expected str for transfer_id")
    if "transferGraphqlId" not in obj:
        raise KeyError("Missing required field 'transferGraphqlId'")
    transfer_graphql_id = obj["transferGraphqlId"]
    if not isinstance(transfer_graphql_id, str):
        raise ValueError("Expected str for transfer_graphql_id")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformTransferAlreadyExistsError(transfer_id, transfer_graphql_id, message)
