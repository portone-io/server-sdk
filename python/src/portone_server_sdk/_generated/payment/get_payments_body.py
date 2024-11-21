from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ..payment.payment_filter_input import PaymentFilterInput, _deserialize_payment_filter_input, _serialize_payment_filter_input

@dataclass
class GetPaymentsBody:
    """결제 건 다건 조회를 위한 입력 정보
    """
    page: Optional[PageInput] = field(default=None)
    """요청할 페이지 정보

    미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
    """
    filter: Optional[PaymentFilterInput] = field(default=None)
    """조회할 결제 건 조건 필터

    V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
    """


def _serialize_get_payments_body(obj: GetPaymentsBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_payment_filter_input(obj.filter)
    return entity


def _deserialize_get_payments_body(obj: Any) -> GetPaymentsBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_payment_filter_input(filter)
    else:
        filter = None
    return GetPaymentsBody(page, filter)
