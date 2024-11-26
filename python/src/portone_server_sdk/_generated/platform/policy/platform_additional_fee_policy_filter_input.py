from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.policy.platform_additional_fee_policy_filter_input_keyword import PlatformAdditionalFeePolicyFilterInputKeyword, _deserialize_platform_additional_fee_policy_filter_input_keyword, _serialize_platform_additional_fee_policy_filter_input_keyword
from ...platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer

@dataclass
class PlatformAdditionalFeePolicyFilterInput:
    """추가 수수료 정책 다건 조회를 위한 필터 조건
    """
    is_archived: Optional[bool] = field(default=None)
    """보관 조회 여부

    true 이면 보관된 추가 수수료 정책의 필터 옵션을 조회하고, false 이면 보관되지 않은 추가 수수료 정책의 필터 옵션을 조회합니다. 기본값은 false 입니다.
    """
    vat_payers: Optional[list[PlatformPayer]] = field(default=None)
    """금액 부담 주체

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 부가세 부담 주체에 해당하는 추가 수수료 정책만 조회합니다.
    """
    keyword: Optional[PlatformAdditionalFeePolicyFilterInputKeyword] = field(default=None)
    """검색 키워드
    """


def _serialize_platform_additional_fee_policy_filter_input(obj: PlatformAdditionalFeePolicyFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.is_archived is not None:
        entity["isArchived"] = obj.is_archived
    if obj.vat_payers is not None:
        entity["vatPayers"] = list(map(_serialize_platform_payer, obj.vat_payers))
    if obj.keyword is not None:
        entity["keyword"] = _serialize_platform_additional_fee_policy_filter_input_keyword(obj.keyword)
    return entity


def _deserialize_platform_additional_fee_policy_filter_input(obj: Any) -> PlatformAdditionalFeePolicyFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "isArchived" in obj:
        is_archived = obj["isArchived"]
        if not isinstance(is_archived, bool):
            raise ValueError(f"{repr(is_archived)} is not bool")
    else:
        is_archived = None
    if "vatPayers" in obj:
        vat_payers = obj["vatPayers"]
        if not isinstance(vat_payers, list):
            raise ValueError(f"{repr(vat_payers)} is not list")
        for i, item in enumerate(vat_payers):
            item = _deserialize_platform_payer(item)
            vat_payers[i] = item
    else:
        vat_payers = None
    if "keyword" in obj:
        keyword = obj["keyword"]
        keyword = _deserialize_platform_additional_fee_policy_filter_input_keyword(keyword)
    else:
        keyword = None
    return PlatformAdditionalFeePolicyFilterInput(is_archived, vat_payers, keyword)
