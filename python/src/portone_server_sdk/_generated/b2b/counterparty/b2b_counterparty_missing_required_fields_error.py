from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyMissingRequiredFieldsError:
    """필수 입력 항목이 누락된 경우

    거래처 생성/수정 시 필수 입력 항목이 누락되었습니다.
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_missing_required_fields_error(obj: B2bCounterpartyMissingRequiredFieldsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_MISSING_REQUIRED_FIELDS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_missing_required_fields_error(obj: Any) -> B2bCounterpartyMissingRequiredFieldsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_MISSING_REQUIRED_FIELDS":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_MISSING_REQUIRED_FIELDS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartyMissingRequiredFieldsError(message)
