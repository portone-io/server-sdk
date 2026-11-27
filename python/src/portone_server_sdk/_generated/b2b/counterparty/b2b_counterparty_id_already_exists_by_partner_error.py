from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyIdAlreadyExistsByPartnerError:
    """파트너 연동으로 생성된 거래처 ID가 이미 사용중인 경우

    파트너 연동으로 생성된 거래처 ID는 재사용할 수 없습니다.
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_id_already_exists_by_partner_error(obj: B2bCounterpartyIdAlreadyExistsByPartnerError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_ID_ALREADY_EXISTS_BY_PARTNER"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_id_already_exists_by_partner_error(obj: Any) -> B2bCounterpartyIdAlreadyExistsByPartnerError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_ID_ALREADY_EXISTS_BY_PARTNER":
        raise ValueError("Expected 'B2B_COUNTERPARTY_ID_ALREADY_EXISTS_BY_PARTNER' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return B2bCounterpartyIdAlreadyExistsByPartnerError(message)
