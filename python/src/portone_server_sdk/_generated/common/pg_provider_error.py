from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PgProviderError:
    """PG사에서 오류를 전달한 경우
    """
    pg_code: str
    pg_message: str
    message: Optional[str] = field(default=None)


def _serialize_pg_provider_error(obj: PgProviderError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PG_PROVIDER"
    entity["pgCode"] = obj.pg_code
    entity["pgMessage"] = obj.pg_message
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_pg_provider_error(obj: Any) -> PgProviderError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PG_PROVIDER":
        raise ValueError(f"{repr(type)} is not 'PG_PROVIDER'")
    if "pgCode" not in obj:
        raise KeyError(f"'pgCode' is not in {obj}")
    pg_code = obj["pgCode"]
    if not isinstance(pg_code, str):
        raise ValueError(f"{repr(pg_code)} is not str")
    if "pgMessage" not in obj:
        raise KeyError(f"'pgMessage' is not in {obj}")
    pg_message = obj["pgMessage"]
    if not isinstance(pg_message, str):
        raise ValueError(f"{repr(pg_message)} is not str")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PgProviderError(pg_code, pg_message, message)
