from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyPartnerNotConnectableError:
    """파트너 연동 거래처는 국세청 연동이 허용되지 않는 경우

    파트너와 연동된 거래처는 국세청 연동을 직접 수행할 수 없습니다.
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_partner_not_connectable_error(obj: B2bCounterpartyPartnerNotConnectableError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_PARTNER_NOT_CONNECTABLE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_partner_not_connectable_error(obj: Any) -> B2bCounterpartyPartnerNotConnectableError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_PARTNER_NOT_CONNECTABLE":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_PARTNER_NOT_CONNECTABLE'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartyPartnerNotConnectableError(message)
