from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.platform.platform_partner_filter_input_keyword import PlatformPartnerFilterInputKeyword, _deserialize_platform_partner_filter_input_keyword, _serialize_platform_partner_filter_input_keyword

@dataclass
class PlatformPartnerFilterInput:
    """파트너 필터 입력 정보
    """
    is_archived: Optional[bool]
    """보관 조회 여부

    true 이면 보관된 파트너를 조회하고, false 이면 보관되지 않은 파트너를 조회합니다. 기본값은 false 입니다.
    """
    tags: Optional[list[str]]
    """하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 태그를 하나 이상 가지는 파트너만 조회합니다.
    """
    banks: Optional[list[Bank]]
    """은행

    하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 은행을 가진 파트너만 조회합니다.
    """
    account_currencies: Optional[list[Currency]]
    """통화 단위

    하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 통화를 가진 파트너만 조회합니다.
    """
    ids: Optional[list[str]]
    """하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 아이디를 가진 파트너만 조회합니다.
    """
    contract_ids: Optional[list[str]]
    """하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 기본 계약 id를 가진 파트너만 조회합니다.
    """
    keyword: Optional[PlatformPartnerFilterInputKeyword]
    """검색 키워드
    """


def _serialize_platform_partner_filter_input(obj: PlatformPartnerFilterInput) -> Any:
    entity = {}
    if obj.is_archived is not None:
        entity["isArchived"] = obj.is_archived
    if obj.tags is not None:
        entity["tags"] = obj.tags
    if obj.banks is not None:
        entity["banks"] = list(map(_serialize_bank, obj.banks))
    if obj.account_currencies is not None:
        entity["accountCurrencies"] = list(map(_serialize_currency, obj.account_currencies))
    if obj.ids is not None:
        entity["ids"] = obj.ids
    if obj.contract_ids is not None:
        entity["contractIds"] = obj.contract_ids
    if obj.keyword is not None:
        entity["keyword"] = _serialize_platform_partner_filter_input_keyword(obj.keyword)
    return entity


def _deserialize_platform_partner_filter_input(obj: Any) -> PlatformPartnerFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "isArchived" in obj:
        is_archived = obj["isArchived"]
        if not isinstance(is_archived, bool):
            raise ValueError(f"{repr(is_archived)} is not bool")
    else:
        is_archived = None
    if "tags" in obj:
        tags = obj["tags"]
        if not isinstance(tags, list):
            raise ValueError(f"{repr(tags)} is not list")
        for i, item in enumerate(tags):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        tags = None
    if "banks" in obj:
        banks = obj["banks"]
        if not isinstance(banks, list):
            raise ValueError(f"{repr(banks)} is not list")
        for i, item in enumerate(banks):
            item = _deserialize_bank(item)
            banks[i] = item
    else:
        banks = None
    if "accountCurrencies" in obj:
        account_currencies = obj["accountCurrencies"]
        if not isinstance(account_currencies, list):
            raise ValueError(f"{repr(account_currencies)} is not list")
        for i, item in enumerate(account_currencies):
            item = _deserialize_currency(item)
            account_currencies[i] = item
    else:
        account_currencies = None
    if "ids" in obj:
        ids = obj["ids"]
        if not isinstance(ids, list):
            raise ValueError(f"{repr(ids)} is not list")
        for i, item in enumerate(ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        ids = None
    if "contractIds" in obj:
        contract_ids = obj["contractIds"]
        if not isinstance(contract_ids, list):
            raise ValueError(f"{repr(contract_ids)} is not list")
        for i, item in enumerate(contract_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        contract_ids = None
    if "keyword" in obj:
        keyword = obj["keyword"]
        keyword = _deserialize_platform_partner_filter_input_keyword(keyword)
    else:
        keyword = None
    return PlatformPartnerFilterInput(is_archived, tags, banks, account_currencies, ids, contract_ids, keyword)
