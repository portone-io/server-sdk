from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartySelfOriginBrnMismatchError:
    """자사 사업자등록번호와 동일한 거래처를 생성할 수 없는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_self_origin_brn_mismatch_error(obj: B2bCounterpartySelfOriginBrnMismatchError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_SELF_ORIGIN_BRN_MISMATCH"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_self_origin_brn_mismatch_error(obj: Any) -> B2bCounterpartySelfOriginBrnMismatchError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_SELF_ORIGIN_BRN_MISMATCH":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_SELF_ORIGIN_BRN_MISMATCH'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartySelfOriginBrnMismatchError(message)
