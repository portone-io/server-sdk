from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeletePlatformTransferResponse:
    pass


def _serialize_delete_platform_transfer_response(obj: DeletePlatformTransferResponse) -> Any:
    entity = {}
    return entity


def _deserialize_delete_platform_transfer_response(obj: Any) -> DeletePlatformTransferResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return DeletePlatformTransferResponse()
