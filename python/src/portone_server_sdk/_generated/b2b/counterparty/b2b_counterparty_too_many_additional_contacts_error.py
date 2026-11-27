from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyTooManyAdditionalContactsError:
    """추가 담당자가 너무 많은 경우

    추가 담당자는 최대 5명까지 등록할 수 있습니다.
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_too_many_additional_contacts_error(obj: B2bCounterpartyTooManyAdditionalContactsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_TOO_MANY_ADDITIONAL_CONTACTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_too_many_additional_contacts_error(obj: Any) -> B2bCounterpartyTooManyAdditionalContactsError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_TOO_MANY_ADDITIONAL_CONTACTS":
        raise ValueError("Expected 'B2B_COUNTERPARTY_TOO_MANY_ADDITIONAL_CONTACTS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return B2bCounterpartyTooManyAdditionalContactsError(message)
