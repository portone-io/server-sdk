from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyBrnModificationNotAllowedError:
    """사업자등록번호 수정이 허용되지 않는 경우

    거래처의 사업자등록번호는 수정할 수 없습니다.
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_brn_modification_not_allowed_error(obj: B2bCounterpartyBrnModificationNotAllowedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_BRN_MODIFICATION_NOT_ALLOWED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_brn_modification_not_allowed_error(obj: Any) -> B2bCounterpartyBrnModificationNotAllowedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_BRN_MODIFICATION_NOT_ALLOWED":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_BRN_MODIFICATION_NOT_ALLOWED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartyBrnModificationNotAllowedError(message)
