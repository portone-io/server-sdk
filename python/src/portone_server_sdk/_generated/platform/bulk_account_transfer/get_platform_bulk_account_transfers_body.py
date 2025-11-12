from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.bulk_account_transfer.platform_bulk_account_transfer_filter_input import PlatformBulkAccountTransferFilterInput, _deserialize_platform_bulk_account_transfer_filter_input, _serialize_platform_bulk_account_transfer_filter_input

@dataclass
class GetPlatformBulkAccountTransfersBody:
    is_for_test: Optional[bool] = field(default=None)
    """Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
    Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
    """
    page: Optional[PageInput] = field(default=None)
    filter: Optional[PlatformBulkAccountTransferFilterInput] = field(default=None)


def _serialize_get_platform_bulk_account_transfers_body(obj: GetPlatformBulkAccountTransfersBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_bulk_account_transfer_filter_input(obj.filter)
    return entity


def _deserialize_get_platform_bulk_account_transfers_body(obj: Any) -> GetPlatformBulkAccountTransfersBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError(f"{repr(is_for_test)} is not bool")
    else:
        is_for_test = None
    if "page" in obj:
        page = obj["page"]
        page = _deserialize_page_input(page)
    else:
        page = None
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_bulk_account_transfer_filter_input(filter)
    else:
        filter = None
    return GetPlatformBulkAccountTransfersBody(is_for_test, page, filter)
