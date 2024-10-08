from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_daily import PlatformSettlementCycleMethodDaily, _deserialize_platform_settlement_cycle_method_daily, _serialize_platform_settlement_cycle_method_daily
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_manual_dates import PlatformSettlementCycleMethodManualDates, _deserialize_platform_settlement_cycle_method_manual_dates, _serialize_platform_settlement_cycle_method_manual_dates
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_monthly import PlatformSettlementCycleMethodMonthly, _deserialize_platform_settlement_cycle_method_monthly, _serialize_platform_settlement_cycle_method_monthly
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_weekly import PlatformSettlementCycleMethodWeekly, _deserialize_platform_settlement_cycle_method_weekly, _serialize_platform_settlement_cycle_method_weekly

PlatformSettlementCycleMethod = Union[PlatformSettlementCycleMethodDaily, PlatformSettlementCycleMethodManualDates, PlatformSettlementCycleMethodMonthly, PlatformSettlementCycleMethodWeekly]
"""플랫폼 정산 주기 계산 방식
"""


def _serialize_platform_settlement_cycle_method(obj: PlatformSettlementCycleMethod) -> Any:
    if obj.type == "DAILY":
        return _serialize_platform_settlement_cycle_method_daily(obj)
    if obj.type == "MANUAL_DATES":
        return _serialize_platform_settlement_cycle_method_manual_dates(obj)
    if obj.type == "MONTHLY":
        return _serialize_platform_settlement_cycle_method_monthly(obj)
    if obj.type == "WEEKLY":
        return _serialize_platform_settlement_cycle_method_weekly(obj)


def _deserialize_platform_settlement_cycle_method(obj: Any) -> PlatformSettlementCycleMethod:
    try:
        return _deserialize_platform_settlement_cycle_method_daily(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_cycle_method_manual_dates(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_cycle_method_monthly(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_cycle_method_weekly(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformSettlementCycleMethod")
