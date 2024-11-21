from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.payout.platform_payout_filter_input import PlatformPayoutFilterInput, _deserialize_platform_payout_filter_input, _serialize_platform_payout_filter_input

@dataclass
class GetPlatformPayoutsBody:
    is_for_test: Optional[bool] = field(default=None)
    page: Optional[PageInput] = field(default=None)
    filter: Optional[PlatformPayoutFilterInput] = field(default=None)


def _serialize_get_platform_payouts_body(obj: GetPlatformPayoutsBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.page is not None:
        entity["page"] = _serialize_page_input(obj.page)
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_payout_filter_input(obj.filter)
    return entity


def _deserialize_get_platform_payouts_body(obj: Any) -> GetPlatformPayoutsBody:
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
        filter = _deserialize_platform_payout_filter_input(filter)
    else:
        filter = None
    return GetPlatformPayoutsBody(is_for_test, page, filter)
