from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_settlement_cycle_date_policy import PlatformSettlementCycleDatePolicy, _deserialize_platform_settlement_cycle_date_policy, _serialize_platform_settlement_cycle_date_policy
from ..platform.platform_settlement_cycle_method import PlatformSettlementCycleMethod, _deserialize_platform_settlement_cycle_method, _serialize_platform_settlement_cycle_method

@dataclass
class PlatformSettlementCycle:
    """정산 주기

    지체일, 정산일, 기준일로 구성되며, 해당 요소들의 조합으로 실제 정산일을 계산합니다.
    """
    lag_days: int
    """지체일 (d+n 의 n)

    정산시작일(통상 주문완료일)로부터 더해진 다음 날짜로부터 가장 가까운 날에 정산이 됩니다. 최소 1 에서 최대 10 까지 지정할 수 있습니다.
    (int32)
    """
    date_policy: PlatformSettlementCycleDatePolicy
    """기준일로, 정산일 계산 시 공휴일을 고려하기 위한 정보입니다.
    """
    method: PlatformSettlementCycleMethod
    """정산 주기 계산 방식
    """


def _serialize_platform_settlement_cycle(obj: PlatformSettlementCycle) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["lagDays"] = obj.lag_days
    entity["datePolicy"] = _serialize_platform_settlement_cycle_date_policy(obj.date_policy)
    entity["method"] = _serialize_platform_settlement_cycle_method(obj.method)
    return entity


def _deserialize_platform_settlement_cycle(obj: Any) -> PlatformSettlementCycle:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "lagDays" not in obj:
        raise KeyError(f"'lagDays' is not in {obj}")
    lag_days = obj["lagDays"]
    if not isinstance(lag_days, int):
        raise ValueError(f"{repr(lag_days)} is not int")
    if "datePolicy" not in obj:
        raise KeyError(f"'datePolicy' is not in {obj}")
    date_policy = obj["datePolicy"]
    date_policy = _deserialize_platform_settlement_cycle_date_policy(date_policy)
    if "method" not in obj:
        raise KeyError(f"'method' is not in {obj}")
    method = obj["method"]
    method = _deserialize_platform_settlement_cycle_method(method)
    return PlatformSettlementCycle(lag_days, date_policy, method)
