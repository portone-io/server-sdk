from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.pg_provider import PgProvider, _deserialize_pg_provider, _serialize_pg_provider
from ..common.selected_channel_type import SelectedChannelType, _deserialize_selected_channel_type, _serialize_selected_channel_type

@dataclass
class SelectedChannel:
    """(결제, 본인인증 등에) 선택된 채널 정보
    """
    type: SelectedChannelType
    """채널 타입
    """
    pg_provider: PgProvider
    """PG사
    """
    pg_merchant_id: str
    """PG사 고객사 식별 아이디
    """
    id: Optional[str] = field(default=None)
    """채널 아이디
    """
    key: Optional[str] = field(default=None)
    """채널 키
    """
    name: Optional[str] = field(default=None)
    """채널 명
    """


def _serialize_selected_channel(obj: SelectedChannel) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = _serialize_selected_channel_type(obj.type)
    entity["pgProvider"] = _serialize_pg_provider(obj.pg_provider)
    entity["pgMerchantId"] = obj.pg_merchant_id
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.key is not None:
        entity["key"] = obj.key
    if obj.name is not None:
        entity["name"] = obj.name
    return entity


def _deserialize_selected_channel(obj: Any) -> SelectedChannel:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_selected_channel_type(type)
    if "pgProvider" not in obj:
        raise KeyError(f"'pgProvider' is not in {obj}")
    pg_provider = obj["pgProvider"]
    pg_provider = _deserialize_pg_provider(pg_provider)
    if "pgMerchantId" not in obj:
        raise KeyError(f"'pgMerchantId' is not in {obj}")
    pg_merchant_id = obj["pgMerchantId"]
    if not isinstance(pg_merchant_id, str):
        raise ValueError(f"{repr(pg_merchant_id)} is not str")
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "key" in obj:
        key = obj["key"]
        if not isinstance(key, str):
            raise ValueError(f"{repr(key)} is not str")
    else:
        key = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    return SelectedChannel(type, pg_provider, pg_merchant_id, id, key, name)
