from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementDateEarlierThanSettlementStartDateError:
    """정산일이 정산 시작일보다 빠른 경우
    """
    settlement_start_date: str
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    settlement_date: str
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_settlement_date_earlier_than_settlement_start_date_error(obj: PlatformSettlementDateEarlierThanSettlementStartDateError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_SETTLEMENT_DATE_EARLIER_THAN_SETTLEMENT_START_DATE"
    entity["settlementStartDate"] = obj.settlement_start_date
    entity["settlementDate"] = obj.settlement_date
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_settlement_date_earlier_than_settlement_start_date_error(obj: Any) -> PlatformSettlementDateEarlierThanSettlementStartDateError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_SETTLEMENT_DATE_EARLIER_THAN_SETTLEMENT_START_DATE":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_SETTLEMENT_DATE_EARLIER_THAN_SETTLEMENT_START_DATE'")
    if "settlementStartDate" not in obj:
        raise KeyError(f"'settlementStartDate' is not in {obj}")
    settlement_start_date = obj["settlementStartDate"]
    if not isinstance(settlement_start_date, str):
        raise ValueError(f"{repr(settlement_start_date)} is not str")
    if "settlementDate" not in obj:
        raise KeyError(f"'settlementDate' is not in {obj}")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError(f"{repr(settlement_date)} is not str")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformSettlementDateEarlierThanSettlementStartDateError(settlement_start_date, settlement_date, message)
