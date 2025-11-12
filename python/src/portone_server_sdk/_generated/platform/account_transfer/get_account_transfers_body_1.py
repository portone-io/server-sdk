from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.account_transfer.platform_account_transfer_filter import PlatformAccountTransferFilter, _deserialize_platform_account_transfer_filter, _serialize_platform_account_transfer_filter

@dataclass
class GetAccountTransfersBody1:
    is_for_test: Optional[bool] = field(default=None)
    """Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
    Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
    """
    page: Optional[PageInput] = field(default=None)
    filter: Optional[PlatformAccountTransferFilter] = field(default=None)


def _serialize_get_account_transfers_body_1(obj: GetAccountTransfersBody1) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_account_transfer_filter(obj.filter)
    return entity


def _deserialize_get_account_transfers_body_1(obj: Any) -> GetAccountTransfersBody1:
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
        filter = _deserialize_platform_account_transfer_filter(filter)
    else:
        filter = None
    return GetAccountTransfersBody1(is_for_test, page, filter)
