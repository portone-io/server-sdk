from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.account_transfer.platform_account_transfer_type import PlatformAccountTransferType, _deserialize_platform_account_transfer_type, _serialize_platform_account_transfer_type

@dataclass
class PlatformAccountTransferFilter:
    types: Optional[list[PlatformAccountTransferType]]
    """계좌 이체 유형
    """


def _serialize_platform_account_transfer_filter(obj: PlatformAccountTransferFilter) -> Any:
    entity = {}
    if obj.types is not None:
        entity["types"] = list(map(_serialize_platform_account_transfer_type, obj.types))
    return entity


def _deserialize_platform_account_transfer_filter(obj: Any) -> PlatformAccountTransferFilter:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "types" in obj:
        types = obj["types"]
        if not isinstance(types, list):
            raise ValueError(f"{repr(types)} is not list")
        for i, item in enumerate(types):
            item = _deserialize_platform_account_transfer_type(item)
            types[i] = item
    else:
        types = None
    return PlatformAccountTransferFilter(types)
