from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.policy.platform_contract_filter_input_keyword import PlatformContractFilterInputKeyword, _deserialize_platform_contract_filter_input_keyword, _serialize_platform_contract_filter_input_keyword
from portone_server_sdk._generated.platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer
from portone_server_sdk._generated.platform.platform_settlement_cycle_date_policy import PlatformSettlementCycleDatePolicy, _deserialize_platform_settlement_cycle_date_policy, _serialize_platform_settlement_cycle_date_policy
from portone_server_sdk._generated.platform.policy.platform_settlement_cycle_type import PlatformSettlementCycleType, _deserialize_platform_settlement_cycle_type, _serialize_platform_settlement_cycle_type

@dataclass
class PlatformContractFilterInput:
    """계약 다건 조회를 위한 필터 조건
    """
    platform_fee_payers: Optional[list[PlatformPayer]]
    """금액 부담 주체

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 수수료 부담 주체를 가진 계약만 조회합니다.
    """
    cycle_types: Optional[list[PlatformSettlementCycleType]]
    """플랫폼 정산 주기 계산 방식

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 주기 계산 방식을 가진 계약만 조회합니다.
    """
    date_policies: Optional[list[PlatformSettlementCycleDatePolicy]]
    """플랫폼 정산 기준일

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 기준일을 가진 계약만 조회합니다.
    """
    is_archived: Optional[bool]
    """보관 조회 여부

    true 이면 보관된 계약을 조회하고, false 이면 보관되지 않은 계약을 조회합니다. 기본값은 false 입니다.
    """
    keyword: Optional[PlatformContractFilterInputKeyword]
    """검색 키워드
    """


def _serialize_platform_contract_filter_input(obj: PlatformContractFilterInput) -> Any:
    entity = {}
    if obj.platform_fee_payers is not None:
        entity["platformFeePayers"] = list(map(_serialize_platform_payer, obj.platform_fee_payers))
    if obj.cycle_types is not None:
        entity["cycleTypes"] = list(map(_serialize_platform_settlement_cycle_type, obj.cycle_types))
    if obj.date_policies is not None:
        entity["datePolicies"] = list(map(_serialize_platform_settlement_cycle_date_policy, obj.date_policies))
    if obj.is_archived is not None:
        entity["isArchived"] = obj.is_archived
    if obj.keyword is not None:
        entity["keyword"] = _serialize_platform_contract_filter_input_keyword(obj.keyword)
    return entity


def _deserialize_platform_contract_filter_input(obj: Any) -> PlatformContractFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "platformFeePayers" in obj:
        platform_fee_payers = obj["platformFeePayers"]
        if not isinstance(platform_fee_payers, list):
            raise ValueError(f"{repr(platform_fee_payers)} is not list")
        for i, item in enumerate(platform_fee_payers):
            item = _deserialize_platform_payer(item)
            platform_fee_payers[i] = item
    else:
        platform_fee_payers = None
    if "cycleTypes" in obj:
        cycle_types = obj["cycleTypes"]
        if not isinstance(cycle_types, list):
            raise ValueError(f"{repr(cycle_types)} is not list")
        for i, item in enumerate(cycle_types):
            item = _deserialize_platform_settlement_cycle_type(item)
            cycle_types[i] = item
    else:
        cycle_types = None
    if "datePolicies" in obj:
        date_policies = obj["datePolicies"]
        if not isinstance(date_policies, list):
            raise ValueError(f"{repr(date_policies)} is not list")
        for i, item in enumerate(date_policies):
            item = _deserialize_platform_settlement_cycle_date_policy(item)
            date_policies[i] = item
    else:
        date_policies = None
    if "isArchived" in obj:
        is_archived = obj["isArchived"]
        if not isinstance(is_archived, bool):
            raise ValueError(f"{repr(is_archived)} is not bool")
    else:
        is_archived = None
    if "keyword" in obj:
        keyword = obj["keyword"]
        keyword = _deserialize_platform_contract_filter_input_keyword(keyword)
    else:
        keyword = None
    return PlatformContractFilterInput(platform_fee_payers, cycle_types, date_policies, is_archived, keyword)
