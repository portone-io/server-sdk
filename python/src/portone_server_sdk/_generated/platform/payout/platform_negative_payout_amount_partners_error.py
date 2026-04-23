from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformNegativePayoutAmountPartnersError:
    """지급 금액의 총합이 음수인 파트너가 존재하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_negative_payout_amount_partners_error(obj: PlatformNegativePayoutAmountPartnersError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CURRENCY_NOT_SUPPORTED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_negative_payout_amount_partners_error(obj: Any) -> PlatformNegativePayoutAmountPartnersError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CURRENCY_NOT_SUPPORTED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CURRENCY_NOT_SUPPORTED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformNegativePayoutAmountPartnersError(message)
