from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_partner_contract_summary import PlatformPartnerContractSummary, _deserialize_platform_partner_contract_summary, _serialize_platform_partner_contract_summary

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
    entity = {}
    entity["tags"] = obj.tags
    entity["contractSummary"] = list(map(_serialize_platform_partner_contract_summary, obj.contract_summary))
    return entity


def _deserialize_platform_partner_filter_options(obj: Any) -> PlatformPartnerFilterOptions:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "tags" not in obj:
        raise KeyError(f"'tags' is not in {obj}")
    tags = obj["tags"]
    if not isinstance(tags, list):
        raise ValueError(f"{repr(tags)} is not list")
    for i, item in enumerate(tags):
        if not isinstance(item, str):
            raise ValueError(f"{repr(item)} is not str")
    if "contractSummary" not in obj:
        raise KeyError(f"'contractSummary' is not in {obj}")
    contract_summary = obj["contractSummary"]
    if not isinstance(contract_summary, list):
        raise ValueError(f"{repr(contract_summary)} is not list")
    for i, item in enumerate(contract_summary):
        item = _deserialize_platform_partner_contract_summary(item)
        contract_summary[i] = item
    return PlatformPartnerFilterOptions(tags, contract_summary)
