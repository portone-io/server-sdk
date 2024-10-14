from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.billing_key.billing_key_filter_input import BillingKeyFilterInput, _deserialize_billing_key_filter_input, _serialize_billing_key_filter_input
from portone_server_sdk._generated.payment.billing_key.billing_key_sort_input import BillingKeySortInput, _deserialize_billing_key_sort_input, _serialize_billing_key_sort_input
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input

@dataclass
class GetBillingKeyInfosBody:
    """빌링키 다건 조회를 위한 입력 정보
    """
    page: Optional[PageInput]
    """요청할 페이지 정보

    미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
    """
    sort: Optional[BillingKeySortInput]
    """정렬 조건

    미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
    """
    filter: Optional[BillingKeyFilterInput]
    """조회할 빌링키 조건 필터

    V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
    """


def _serialize_get_billing_key_infos_body(obj: GetBillingKeyInfosBody) -> Any:
    entity = {}
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.sort is not None:
        entity["sort"] = _serialize_billing_key_sort_input(obj.sort)
    if obj.filter is not None:
        entity["filter"] = _serialize_billing_key_filter_input(obj.filter)
    return entity


def _deserialize_get_billing_key_infos_body(obj: Any) -> GetBillingKeyInfosBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "sort" in obj:
        sort = obj["sort"]
        sort = _deserialize_billing_key_sort_input(sort)
    else:
        sort = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_billing_key_filter_input(filter)
    else:
        filter = None
    return GetBillingKeyInfosBody(page, sort, filter)
