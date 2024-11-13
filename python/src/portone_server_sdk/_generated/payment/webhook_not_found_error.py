from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookNotFoundError:
    """웹훅 내역이 존재하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_webhook_not_found_error(obj: WebhookNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "WEBHOOK_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_webhook_not_found_error(obj: Any) -> WebhookNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "WEBHOOK_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'WEBHOOK_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return WebhookNotFoundError(message)
