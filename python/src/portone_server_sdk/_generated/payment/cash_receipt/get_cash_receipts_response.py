from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.cash_receipt.cash_receipt import CashReceipt, _deserialize_cash_receipt, _serialize_cash_receipt
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info

@dataclass
class GetCashReceiptsResponse:
    """현금영수증 다건 조회 성공 응답 정보
    """
    items: list[CashReceipt]
    """조회된 현금영수증 리스트
    """
    page: PageInfo
    """조회된 페이지 정보
    """


def _serialize_get_cash_receipts_response(obj: GetCashReceiptsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_cash_receipt, obj.items))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_cash_receipts_response(obj: Any) -> GetCashReceiptsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_cash_receipt(item)
        items[i] = item
    if "page" not in obj:
        raise KeyError(f"'page' is not in {obj}")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetCashReceiptsResponse(items, page)
