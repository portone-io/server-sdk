from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookNotFoundError:
    """웹훅 내역이 존재하지 않는 경우
    """
    type: Literal["WEBHOOK_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_webhook_not_found_error(obj: WebhookNotFoundError) -> Any:
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
    return WebhookNotFoundError(type, message)
