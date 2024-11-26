from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.payment_schedule.payment_schedule_status import PaymentScheduleStatus, _deserialize_payment_schedule_status, _serialize_payment_schedule_status

@dataclass
class PaymentScheduleFilterInput:
    """결제 예약 건 다건 조회를 위한 입력 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    billing_key: Optional[str] = field(default=None)
    """빌링키
    """
    from_: Optional[str] = field(default=None)
    """결제 예정 시점 조건 범위의 시작

    값을 입력하지 않으면 파라미터 end의 90일 전으로 설정됩니다.
    (RFC 3339 date-time)
    """
    until: Optional[str] = field(default=None)
    """결제 예정 시점 조건 범위의 끝

    값을 입력하지 않으면 현재 시점으로 설정됩니다.
    (RFC 3339 date-time)
    """
    status: Optional[list[PaymentScheduleStatus]] = field(default=None)
    """결제 예약 건 상태 리스트

    값을 입력하지 않으면 상태 필터링이 적용되지 않습니다.
    """


def _serialize_payment_schedule_filter_input(obj: PaymentScheduleFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.billing_key is not None:
        entity["billingKey"] = obj.billing_key
    if obj.from_ is not None:
        entity["from"] = obj.from_
    if obj.until is not None:
        entity["until"] = obj.until
    if obj.status is not None:
        entity["status"] = list(map(_serialize_payment_schedule_status, obj.status))
    return entity


def _deserialize_payment_schedule_filter_input(obj: Any) -> PaymentScheduleFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "billingKey" in obj:
        billing_key = obj["billingKey"]
        if not isinstance(billing_key, str):
            raise ValueError(f"{repr(billing_key)} is not str")
    else:
        billing_key = None
    if "from" in obj:
        from_ = obj["from"]
        if not isinstance(from_, str):
            raise ValueError(f"{repr(from_)} is not str")
    else:
        from_ = None
    if "until" in obj:
        until = obj["until"]
        if not isinstance(until, str):
            raise ValueError(f"{repr(until)} is not str")
    else:
        until = None
    if "status" in obj:
        status = obj["status"]
        if not isinstance(status, list):
            raise ValueError(f"{repr(status)} is not list")
        for i, item in enumerate(status):
            item = _deserialize_payment_schedule_status(item)
            status[i] = item
    else:
        status = None
    return PaymentScheduleFilterInput(store_id, billing_key, from_, until, status)
