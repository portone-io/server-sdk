from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformTransferAlreadyExistsError:
    type: Literal["PLATFORM_TRANSFER_ALREADY_EXISTS"] = field(repr=False)
    transfer_id: str
    transfer_graphql_id: str
    message: Optional[str]


def _serialize_platform_transfer_already_exists_error(obj: PlatformTransferAlreadyExistsError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_TRANSFER_ALREADY_EXISTS"
    entity["transferId"] = obj.transfer_id
    entity["transferGraphqlId"] = obj.transfer_graphql_id
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_transfer_already_exists_error(obj: Any) -> PlatformTransferAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_TRANSFER_ALREADY_EXISTS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_TRANSFER_ALREADY_EXISTS'")
    if "transferId" not in obj:
        raise KeyError(f"'transferId' is not in {obj}")
    transfer_id = obj["transferId"]
    if not isinstance(transfer_id, str):
        raise ValueError(f"{repr(transfer_id)} is not str")
    if "transferGraphqlId" not in obj:
        raise KeyError(f"'transferGraphqlId' is not in {obj}")
    transfer_graphql_id = obj["transferGraphqlId"]
    if not isinstance(transfer_graphql_id, str):
        raise ValueError(f"{repr(transfer_graphql_id)} is not str")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformTransferAlreadyExistsError(type, transfer_id, transfer_graphql_id, message)
