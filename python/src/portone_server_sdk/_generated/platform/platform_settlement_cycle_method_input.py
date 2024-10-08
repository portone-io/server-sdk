from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_daily_input import PlatformSettlementCycleMethodDailyInput, _deserialize_platform_settlement_cycle_method_daily_input, _serialize_platform_settlement_cycle_method_daily_input
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_manual_dates_input import PlatformSettlementCycleMethodManualDatesInput, _deserialize_platform_settlement_cycle_method_manual_dates_input, _serialize_platform_settlement_cycle_method_manual_dates_input
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_monthly_input import PlatformSettlementCycleMethodMonthlyInput, _deserialize_platform_settlement_cycle_method_monthly_input, _serialize_platform_settlement_cycle_method_monthly_input
from portone_server_sdk._generated.platform.platform_settlement_cycle_method_weekly_input import PlatformSettlementCycleMethodWeeklyInput, _deserialize_platform_settlement_cycle_method_weekly_input, _serialize_platform_settlement_cycle_method_weekly_input

@dataclass
class PlatformSettlementCycleMethodInput:
    """플랫폼 정산 주기 계산 방식 입력 정보

    하나의 하위 필드에만 값을 명시하여 요청합니다.
    """
    daily: Optional[PlatformSettlementCycleMethodDailyInput]
    """매일 정산
    """
    weekly: Optional[PlatformSettlementCycleMethodWeeklyInput]
    """매주 정해진 요일에 정산
    """
    monthly: Optional[PlatformSettlementCycleMethodMonthlyInput]
    """매월 정해진 날(일)에 정산
    """
    manual_dates: Optional[PlatformSettlementCycleMethodManualDatesInput]
    """정해진 날짜(월, 일)에 정산
    """


def _serialize_platform_settlement_cycle_method_input(obj: PlatformSettlementCycleMethodInput) -> Any:
    entity = {}
    if obj.daily is not None:
        entity["daily"] = _serialize_platform_settlement_cycle_method_daily_input(obj.daily)
    if obj.weekly is not None:
        entity["weekly"] = _serialize_platform_settlement_cycle_method_weekly_input(obj.weekly)
    if obj.monthly is not None:
        entity["monthly"] = _serialize_platform_settlement_cycle_method_monthly_input(obj.monthly)
    if obj.manual_dates is not None:
        entity["manualDates"] = _serialize_platform_settlement_cycle_method_manual_dates_input(obj.manual_dates)
    return entity


def _deserialize_platform_settlement_cycle_method_input(obj: Any) -> PlatformSettlementCycleMethodInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "daily" in obj:
        daily = obj["daily"]
        daily = _deserialize_platform_settlement_cycle_method_daily_input(daily)
    else:
        daily = None
    if "weekly" in obj:
        weekly = obj["weekly"]
        weekly = _deserialize_platform_settlement_cycle_method_weekly_input(weekly)
    else:
        weekly = None
    if "monthly" in obj:
        monthly = obj["monthly"]
        monthly = _deserialize_platform_settlement_cycle_method_monthly_input(monthly)
    else:
        monthly = None
    if "manualDates" in obj:
        manual_dates = obj["manualDates"]
        manual_dates = _deserialize_platform_settlement_cycle_method_manual_dates_input(manual_dates)
    else:
        manual_dates = None
    return PlatformSettlementCycleMethodInput(daily, weekly, monthly, manual_dates)
