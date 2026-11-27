from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.page_info import PageInfo, _deserialize_page_info, _serialize_page_info
from ...platform.transfer.platform_transfer_summary import PlatformTransferSummary, _deserialize_platform_transfer_summary, _serialize_platform_transfer_summary

@dataclass
class GetPlatformTransferSummariesResponse:
    transfer_summaries: list[PlatformTransferSummary]
    page: PageInfo


def _serialize_get_platform_transfer_summaries_response(obj: GetPlatformTransferSummariesResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["transferSummaries"] = list(map(_serialize_platform_transfer_summary, obj.transfer_summaries))
    entity["page"] = _serialize_page_info(obj.page)
    return entity


def _deserialize_get_platform_transfer_summaries_response(obj: Any) -> GetPlatformTransferSummariesResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "transferSummaries" not in obj:
        raise KeyError("Missing required field 'transferSummaries'")
    transfer_summaries = obj["transferSummaries"]
    if not isinstance(transfer_summaries, list):
        raise ValueError("Expected list for transfer_summaries")
    for i, item in enumerate(transfer_summaries):
        item = _deserialize_platform_transfer_summary(item)
        transfer_summaries[i] = item
    if "page" not in obj:
        raise KeyError("Missing required field 'page'")
    page = obj["page"]
    page = _deserialize_page_info(page)
    return GetPlatformTransferSummariesResponse(transfer_summaries, page)
