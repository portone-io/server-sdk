from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.get_b2b_tax_invoices_body_filter import GetB2bTaxInvoicesBodyFilter, _deserialize_get_b2b_tax_invoices_body_filter, _serialize_get_b2b_tax_invoices_body_filter

@dataclass
class GetB2bTaxInvoicesBody:
    """세금 계산서 다건 조회를 위한 입력 정보
    """
    test: Optional[bool] = field(default=None)
    """테스트 모드 여부

    true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
    """
    page_number: Optional[int] = field(default=None)
    """페이지 번호

    0부터 시작하는 페이지 번호. 기본 값은 0.
    (int32)
    """
    page_size: Optional[int] = field(default=None)
    """페이지 크기

    각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
    (int32)
    """
    filter: Optional[GetB2bTaxInvoicesBodyFilter] = field(default=None)
    """필터
    """


def _serialize_get_b2b_tax_invoices_body(obj: GetB2bTaxInvoicesBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.test is not None:
        entity["test"] = obj.test
    if obj.page_number is not None:
        entity["pageNumber"] = obj.page_number
    if obj.page_size is not None:
        entity["pageSize"] = obj.page_size
    if obj.filter is not None:
        entity["filter"] = _serialize_get_b2b_tax_invoices_body_filter(obj.filter)
    return entity


def _deserialize_get_b2b_tax_invoices_body(obj: Any) -> GetB2bTaxInvoicesBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "test" in obj:
        test = obj["test"]
        if not isinstance(test, bool):
            raise ValueError(f"{repr(test)} is not bool")
    else:
        test = None
    if "pageNumber" in obj:
        page_number = obj["pageNumber"]
        if not isinstance(page_number, int):
            raise ValueError(f"{repr(page_number)} is not int")
    else:
        page_number = None
    if "pageSize" in obj:
        page_size = obj["pageSize"]
        if not isinstance(page_size, int):
            raise ValueError(f"{repr(page_size)} is not int")
    else:
        page_size = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_get_b2b_tax_invoices_body_filter(filter)
    else:
        filter = None
    return GetB2bTaxInvoicesBody(test, page_number, page_size, filter)
