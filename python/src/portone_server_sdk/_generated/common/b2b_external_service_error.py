from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bExternalServiceError:
    """외부 서비스에서 에러가 발생한 경우
    """
    type: Literal["B2B_EXTERNAL_SERVICE"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_external_service_error(obj: B2bExternalServiceError) -> Any:
    entity = {}
    entity["type"] = "B2B_EXTERNAL_SERVICE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_external_service_error(obj: Any) -> B2bExternalServiceError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_EXTERNAL_SERVICE":
        raise ValueError(f"{repr(type)} is not 'B2B_EXTERNAL_SERVICE'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bExternalServiceError(type, message)
