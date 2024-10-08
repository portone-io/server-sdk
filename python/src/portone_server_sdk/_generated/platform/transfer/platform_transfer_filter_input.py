from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.date_range import DateRange, _deserialize_date_range, _serialize_date_range
from portone_server_sdk._generated.common.payment_method_type import PaymentMethodType, _deserialize_payment_method_type, _serialize_payment_method_type
from portone_server_sdk._generated.platform.transfer.platform_transfer_filter_input_keyword import PlatformTransferFilterInputKeyword, _deserialize_platform_transfer_filter_input_keyword, _serialize_platform_transfer_filter_input_keyword
from portone_server_sdk._generated.platform.transfer.platform_transfer_status import PlatformTransferStatus, _deserialize_platform_transfer_status, _serialize_platform_transfer_status
from portone_server_sdk._generated.platform.transfer.platform_transfer_type import PlatformTransferType, _deserialize_platform_transfer_type, _serialize_platform_transfer_type

@dataclass
class PlatformTransferFilterInput:
    """정산건 필터 입력 정보

    정산 시작일 범위와 정산 일 범위는 둘 중 하나만 입력 가능합니다.
    """
    settlement_start_date_range: Optional[DateRange]
    """정산 시작일 범위
    """
    settlement_date_range: Optional[DateRange]
    """정산 일 범위
    """
    partner_tags: Optional[list[str]]
    """파트너 태그 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 태그를 하나 이상 가지는 파트너에 대한 정산건만 조회합니다.
    """
    contract_ids: Optional[list[str]]
    """계약 아이디 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 계약 아이디를 가지는 정산건만 조회합니다.
    """
    discount_share_policy_ids: Optional[list[str]]
    """할인 분담 정책 아이디 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 할인 분담 정책 아이디를 하나 이상 가지는 정산건만 조회합니다.
    """
    additional_fee_policy_ids: Optional[list[str]]
    """추가 수수료 정책 아이디 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 추가 수수료 아이디를 하나 이상 가지는 정산건만 조회합니다.
    """
    payment_method_types: Optional[list[PaymentMethodType]]
    """결제 수단 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 결제 수단을 가지는 파트너만 조회합니다.
    """
    channel_keys: Optional[list[str]]
    """채널 키 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 채널 키를 가지는 정산건만 조회합니다.
    """
    types: Optional[list[PlatformTransferType]]
    """정산 방식 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 방식의 정산건만 조회합니다.
    """
    statuses: Optional[list[PlatformTransferStatus]]
    """정산 상태 리스트

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 정산 상태인 정산건만 조회합니다.
    """
    keyword: Optional[PlatformTransferFilterInputKeyword]
    """검색 키워드
    """
    is_for_test: Optional[bool]
    """테스트 모드 여부
    """


def _serialize_platform_transfer_filter_input(obj: PlatformTransferFilterInput) -> Any:
    entity = {}
    if obj.settlement_start_date_range is not None:
        entity["settlementStartDateRange"] = _serialize_date_range(obj.settlement_start_date_range)
    if obj.settlement_date_range is not None:
        entity["settlementDateRange"] = _serialize_date_range(obj.settlement_date_range)
    if obj.partner_tags is not None:
        entity["partnerTags"] = obj.partner_tags
    if obj.contract_ids is not None:
        entity["contractIds"] = obj.contract_ids
    if obj.discount_share_policy_ids is not None:
        entity["discountSharePolicyIds"] = obj.discount_share_policy_ids
    if obj.additional_fee_policy_ids is not None:
        entity["additionalFeePolicyIds"] = obj.additional_fee_policy_ids
    if obj.payment_method_types is not None:
        entity["paymentMethodTypes"] = list(map(_serialize_payment_method_type, obj.payment_method_types))
    if obj.channel_keys is not None:
        entity["channelKeys"] = obj.channel_keys
    if obj.types is not None:
        entity["types"] = list(map(_serialize_platform_transfer_type, obj.types))
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_platform_transfer_status, obj.statuses))
    if obj.keyword is not None:
        entity["keyword"] = _serialize_platform_transfer_filter_input_keyword(obj.keyword)
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    return entity


def _deserialize_platform_transfer_filter_input(obj: Any) -> PlatformTransferFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "settlementStartDateRange" in obj:
        settlement_start_date_range = obj["settlementStartDateRange"]
        settlement_start_date_range = _deserialize_date_range(settlement_start_date_range)
    else:
        settlement_start_date_range = None
    if "settlementDateRange" in obj:
        settlement_date_range = obj["settlementDateRange"]
        settlement_date_range = _deserialize_date_range(settlement_date_range)
    else:
        settlement_date_range = None
    if "partnerTags" in obj:
        partner_tags = obj["partnerTags"]
        if not isinstance(partner_tags, list):
            raise ValueError(f"{repr(partner_tags)} is not list")
        for i, item in enumerate(partner_tags):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        partner_tags = None
    if "contractIds" in obj:
        contract_ids = obj["contractIds"]
        if not isinstance(contract_ids, list):
            raise ValueError(f"{repr(contract_ids)} is not list")
        for i, item in enumerate(contract_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        contract_ids = None
    if "discountSharePolicyIds" in obj:
        discount_share_policy_ids = obj["discountSharePolicyIds"]
        if not isinstance(discount_share_policy_ids, list):
            raise ValueError(f"{repr(discount_share_policy_ids)} is not list")
        for i, item in enumerate(discount_share_policy_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        discount_share_policy_ids = None
    if "additionalFeePolicyIds" in obj:
        additional_fee_policy_ids = obj["additionalFeePolicyIds"]
        if not isinstance(additional_fee_policy_ids, list):
            raise ValueError(f"{repr(additional_fee_policy_ids)} is not list")
        for i, item in enumerate(additional_fee_policy_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        additional_fee_policy_ids = None
    if "paymentMethodTypes" in obj:
        payment_method_types = obj["paymentMethodTypes"]
        if not isinstance(payment_method_types, list):
            raise ValueError(f"{repr(payment_method_types)} is not list")
        for i, item in enumerate(payment_method_types):
            item = _deserialize_payment_method_type(item)
            payment_method_types[i] = item
    else:
        payment_method_types = None
    if "channelKeys" in obj:
        channel_keys = obj["channelKeys"]
        if not isinstance(channel_keys, list):
            raise ValueError(f"{repr(channel_keys)} is not list")
        for i, item in enumerate(channel_keys):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        channel_keys = None
    if "types" in obj:
        types = obj["types"]
        if not isinstance(types, list):
            raise ValueError(f"{repr(types)} is not list")
        for i, item in enumerate(types):
            item = _deserialize_platform_transfer_type(item)
            types[i] = item
    else:
        types = None
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_platform_transfer_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "keyword" in obj:
        keyword = obj["keyword"]
        keyword = _deserialize_platform_transfer_filter_input_keyword(keyword)
    else:
        keyword = None
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError(f"{repr(is_for_test)} is not bool")
    else:
        is_for_test = None
    return PlatformTransferFilterInput(settlement_start_date_range, settlement_date_range, partner_tags, contract_ids, discount_share_policy_ids, additional_fee_policy_ids, payment_method_types, channel_keys, types, statuses, keyword, is_for_test)
