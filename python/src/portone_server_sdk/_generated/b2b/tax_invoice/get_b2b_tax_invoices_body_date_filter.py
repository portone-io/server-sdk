from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.tax_invoice.b2b_search_date_type import B2bSearchDateType, _deserialize_b2b_search_date_type, _serialize_b2b_search_date_type
from portone_server_sdk._generated.b2b.tax_invoice.date_range_option import DateRangeOption, _deserialize_date_range_option, _serialize_date_range_option

@dataclass
class GetB2bTaxInvoicesBodyDateFilter:
    """조회 기간 필터
    """
    date_type: Optional[B2bSearchDateType]
    """조회 기간 기준

    미입력시 기본값은 등록일(`REGISTER`)로 설정됩니다.
    """
    date_range: Optional[list[DateRangeOption]]
    """조회 기간

    미입력시 `dateRange.from`의 기본값은 한 달 이전, `dateRange.until`의 기본값은 현재 일자로 설정됩니다.
    """


def _serialize_get_b2b_tax_invoices_body_date_filter(obj: GetB2bTaxInvoicesBodyDateFilter) -> Any:
    entity = {}
    if obj.date_type is not None:
        entity["dateType"] = _serialize_b2b_search_date_type(obj.date_type)
    if obj.date_range is not None:
        entity["dateRange"] = list(map(_serialize_date_range_option, obj.date_range))
    return entity


def _deserialize_get_b2b_tax_invoices_body_date_filter(obj: Any) -> GetB2bTaxInvoicesBodyDateFilter:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "dateType" in obj:
        date_type = obj["dateType"]
        date_type = _deserialize_b2b_search_date_type(date_type)
    else:
        date_type = None
    if "dateRange" in obj:
        date_range = obj["dateRange"]
        if not isinstance(date_range, list):
            raise ValueError(f"{repr(date_range)} is not list")
        for i, item in enumerate(date_range):
            item = _deserialize_date_range_option(item)
            date_range[i] = item
    else:
        date_range = None
    return GetB2bTaxInvoicesBodyDateFilter(date_type, date_range)
