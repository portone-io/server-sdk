from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_partner_contract_summary import PlatformPartnerContractSummary, _deserialize_platform_partner_contract_summary, _serialize_platform_partner_contract_summary

@dataclass
class PlatformPartnerFilterOptions:
    """파트너 필터 옵션 조회 성공 응답 정보
    """
    tags: list[str]
    """조회된 태그 리스트
    """
    contract_summary: list[PlatformPartnerContractSummary]
    """조회된 파트너 계약 요약 정보 리스트
    """


def _serialize_platform_partner_filter_options(obj: PlatformPartnerFilterOptions) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["tags"] = obj.tags
    entity["contractSummary"] = list(map(_serialize_platform_partner_contract_summary, obj.contract_summary))
    return entity


def _deserialize_platform_partner_filter_options(obj: Any) -> PlatformPartnerFilterOptions:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "tags" not in obj:
        raise KeyError("Missing required field 'tags'")
    tags = obj["tags"]
    if not isinstance(tags, list):
        raise ValueError("Expected list for tags")
    for i, item in enumerate(tags):
        if not isinstance(item, str):
            raise ValueError("Expected str for item")
    if "contractSummary" not in obj:
        raise KeyError("Missing required field 'contractSummary'")
    contract_summary = obj["contractSummary"]
    if not isinstance(contract_summary, list):
        raise ValueError("Expected list for contract_summary")
    for i, item in enumerate(contract_summary):
        item = _deserialize_platform_partner_contract_summary(item)
        contract_summary[i] = item
    return PlatformPartnerFilterOptions(tags, contract_summary)
