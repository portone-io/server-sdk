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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PG_PROVIDER":
        raise ValueError("Expected 'PG_PROVIDER' for type")
    if "pgCode" not in obj:
        raise KeyError("Missing required field 'pgCode'")
    pg_code = obj["pgCode"]
    if not isinstance(pg_code, str):
        raise ValueError("Expected str for pg_code")
    if "pgMessage" not in obj:
        raise KeyError("Missing required field 'pgMessage'")
    pg_message = obj["pgMessage"]
    if not isinstance(pg_message, str):
        raise ValueError("Expected str for pg_message")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PgProviderError(pg_code, pg_message, message)
