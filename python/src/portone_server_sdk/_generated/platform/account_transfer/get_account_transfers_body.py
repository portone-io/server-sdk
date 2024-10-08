from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.platform.account_transfer.platform_account_transfer_filter import PlatformAccountTransferFilter, _deserialize_platform_account_transfer_filter, _serialize_platform_account_transfer_filter

@dataclass
class GetAccountTransfersBody:
    is_for_test: Optional[bool]
    page: Optional[PageInput]
    filter: Optional[PlatformAccountTransferFilter]


def _serialize_get_account_transfers_body(obj: GetAccountTransfersBody) -> Any:
    entity = {}
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_account_transfer_filter(obj.filter)
    return entity


def _deserialize_get_account_transfers_body(obj: Any) -> GetAccountTransfersBody:
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
    return GetAccountTransfersBody(is_for_test, page, filter)
