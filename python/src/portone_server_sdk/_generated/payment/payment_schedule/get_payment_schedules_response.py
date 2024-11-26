from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from ...payment.payment_schedule.payment_schedule import PaymentSchedule, _deserialize_payment_schedule, _serialize_payment_schedule

@dataclass
class GetPaymentSchedulesResponse:
    """결제 예약 다건 조회 성공 응답 정보
    """
    items: list[PaymentSchedule]
    """조회된 결제 예약 건 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_payment_schedules_response(obj: GetPaymentSchedulesResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_payment_schedule, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_payment_schedules_response(obj: Any) -> GetPaymentSchedulesResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_payment_schedule(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetPaymentSchedulesResponse(items, page)
