from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...payment.payment_schedule.payment_schedule_filter_input import PaymentScheduleFilterInput, _deserialize_payment_schedule_filter_input, _serialize_payment_schedule_filter_input
from ...payment.payment_schedule.payment_schedule_sort_input import PaymentScheduleSortInput, _deserialize_payment_schedule_sort_input, _serialize_payment_schedule_sort_input

@dataclass
class GetPaymentSchedulesBody:
    """결제 예약 다건 조회를 위한 입력 정보

    조회 결과는 결제 예정 시점(timeToPay) 기준 최신 순으로 정렬됩니다.
    """
    page: Optional[PageInput] = field(default=None)
    """요청할 페이지 정보

    미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
    """
    sort: Optional[PaymentScheduleSortInput] = field(default=None)
    """정렬 조건

    미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
    """
    filter: Optional[PaymentScheduleFilterInput] = field(default=None)
    """조회할 결제 예약 건의 조건 필터
    """


def _serialize_get_payment_schedules_body(obj: GetPaymentSchedulesBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.sort is not None:
        entity["sort"] = _serialize_payment_schedule_sort_input(obj.sort)
    if obj.filter is not None:
        entity["filter"] = _serialize_payment_schedule_filter_input(obj.filter)
    return entity


def _deserialize_get_payment_schedules_body(obj: Any) -> GetPaymentSchedulesBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "sort" in obj:
        sort = obj["sort"]
        sort = _deserialize_payment_schedule_sort_input(sort)
    else:
        sort = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_payment_schedule_filter_input(filter)
    else:
        filter = None
    return GetPaymentSchedulesBody(page, sort, filter)
