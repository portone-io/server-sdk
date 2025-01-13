from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.bank import Bank, _deserialize_bank, _serialize_bank
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..platform.platform_account_status import PlatformAccountStatus, _deserialize_platform_account_status, _serialize_platform_account_status
from ..platform.platform_partner_business_status import PlatformPartnerBusinessStatus, _deserialize_platform_partner_business_status, _serialize_platform_partner_business_status
from ..platform.platform_partner_filter_input_keyword import PlatformPartnerFilterInputKeyword, _deserialize_platform_partner_filter_input_keyword, _serialize_platform_partner_filter_input_keyword
from ..platform.platform_partner_member_company_connection_status import PlatformPartnerMemberCompanyConnectionStatus, _deserialize_platform_partner_member_company_connection_status, _serialize_platform_partner_member_company_connection_status
from ..platform.platform_partner_taxation_type import PlatformPartnerTaxationType, _deserialize_platform_partner_taxation_type, _serialize_platform_partner_taxation_type
from ..platform.platform_partner_type_name import PlatformPartnerTypeName, _deserialize_platform_partner_type_name, _serialize_platform_partner_type_name

@dataclass
class PlatformPartnerFilterInput:
    """파트너 필터 입력 정보
    """
    is_archived: Optional[bool] = field(default=None)
    """보관 조회 여부

    true 이면 보관된 파트너를 조회하고, false 이면 보관되지 않은 파트너를 조회합니다. 기본값은 false 입니다.
    """
    tags: Optional[list[str]] = field(default=None)
    """하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 태그를 하나 이상 가지는 파트너만 조회합니다.
    """
    banks: Optional[list[Bank]] = field(default=None)
    """은행

    하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 은행을 가진 파트너만 조회합니다.
    """
    account_currencies: Optional[list[Currency]] = field(default=None)
    """통화 단위

    하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 통화를 가진 파트너만 조회합니다.
    """
    ids: Optional[list[str]] = field(default=None)
    """하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 아이디를 가진 파트너만 조회합니다.
    """
    contract_ids: Optional[list[str]] = field(default=None)
    """하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 기본 계약 id를 가진 파트너만 조회합니다.
    """
    account_statuses: Optional[list[PlatformAccountStatus]] = field(default=None)
    """플랫폼 계좌 상태

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 계좌 상태를 가진 파트너만 조회합니다.
    """
    business_statuses: Optional[list[PlatformPartnerBusinessStatus]] = field(default=None)
    """플랫폼 파트너 사업자 상태

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 사업자 상태를 가진 파트너만 조회합니다.
    """
    types: Optional[list[PlatformPartnerTypeName]] = field(default=None)
    """플랫폼 파트너 유형 이름

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 사업자 유형을 가진 파트너만 조회합니다.
    """
    taxation_types: Optional[list[PlatformPartnerTaxationType]] = field(default=None)
    """플랫폼 파트너 과세 유형

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 과세 유형을 가진 파트너만 조회합니다.
    """
    member_company_connection_statuses: Optional[list[PlatformPartnerMemberCompanyConnectionStatus]] = field(default=None)
    """플랫폼 파트너 연동 사업자 연결 상태

    하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 연동 사업자 연결 상태를 가진 파트너만 조회합니다.
    """
    keyword: Optional[PlatformPartnerFilterInputKeyword] = field(default=None)
    """검색 키워드
    """


def _serialize_platform_partner_filter_input(obj: PlatformPartnerFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
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
    if obj.account_statuses is not None:
        entity["accountStatuses"] = list(map(_serialize_platform_account_status, obj.account_statuses))
    if obj.business_statuses is not None:
        entity["businessStatuses"] = list(map(_serialize_platform_partner_business_status, obj.business_statuses))
    if obj.types is not None:
        entity["types"] = list(map(_serialize_platform_partner_type_name, obj.types))
    if obj.taxation_types is not None:
        entity["taxationTypes"] = list(map(_serialize_platform_partner_taxation_type, obj.taxation_types))
    if obj.member_company_connection_statuses is not None:
        entity["memberCompanyConnectionStatuses"] = list(map(_serialize_platform_partner_member_company_connection_status, obj.member_company_connection_statuses))
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
    if "accountStatuses" in obj:
        account_statuses = obj["accountStatuses"]
        if not isinstance(account_statuses, list):
            raise ValueError(f"{repr(account_statuses)} is not list")
        for i, item in enumerate(account_statuses):
            item = _deserialize_platform_account_status(item)
            account_statuses[i] = item
    else:
        account_statuses = None
    if "businessStatuses" in obj:
        business_statuses = obj["businessStatuses"]
        if not isinstance(business_statuses, list):
            raise ValueError(f"{repr(business_statuses)} is not list")
        for i, item in enumerate(business_statuses):
            item = _deserialize_platform_partner_business_status(item)
            business_statuses[i] = item
    else:
        business_statuses = None
    if "types" in obj:
        types = obj["types"]
        if not isinstance(types, list):
            raise ValueError(f"{repr(types)} is not list")
        for i, item in enumerate(types):
            item = _deserialize_platform_partner_type_name(item)
            types[i] = item
    else:
        types = None
    if "taxationTypes" in obj:
        taxation_types = obj["taxationTypes"]
        if not isinstance(taxation_types, list):
            raise ValueError(f"{repr(taxation_types)} is not list")
        for i, item in enumerate(taxation_types):
            item = _deserialize_platform_partner_taxation_type(item)
            taxation_types[i] = item
    else:
        taxation_types = None
    if "memberCompanyConnectionStatuses" in obj:
        member_company_connection_statuses = obj["memberCompanyConnectionStatuses"]
        if not isinstance(member_company_connection_statuses, list):
            raise ValueError(f"{repr(member_company_connection_statuses)} is not list")
        for i, item in enumerate(member_company_connection_statuses):
            item = _deserialize_platform_partner_member_company_connection_status(item)
            member_company_connection_statuses[i] = item
    else:
        member_company_connection_statuses = None
    if "keyword" in obj:
        keyword = obj["keyword"]
        keyword = _deserialize_platform_partner_filter_input_keyword(keyword)
    else:
        keyword = None
    return PlatformPartnerFilterInput(is_archived, tags, banks, account_currencies, ids, contract_ids, account_statuses, business_statuses, types, taxation_types, member_company_connection_statuses, keyword)
