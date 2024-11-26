from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.partner_settlement.platform_partner_settlement_filter_keyword_input import PlatformPartnerSettlementFilterKeywordInput, _deserialize_platform_partner_settlement_filter_keyword_input, _serialize_platform_partner_settlement_filter_keyword_input
from ...platform.partner_settlement.platform_partner_settlement_status import PlatformPartnerSettlementStatus, _deserialize_platform_partner_settlement_status, _serialize_platform_partner_settlement_status
from ...platform.partner_settlement.platform_partner_settlement_type import PlatformPartnerSettlementType, _deserialize_platform_partner_settlement_type, _serialize_platform_partner_settlement_type

@dataclass
class PlatformPartnerSettlementFilterInput:
    settlement_dates: Optional[list[str]] = field(default=None)
    contract_ids: Optional[list[str]] = field(default=None)
    partner_tags: Optional[list[str]] = field(default=None)
    settlement_currencies: Optional[list[Currency]] = field(default=None)
    """통화 단위
    """
    statuses: Optional[list[PlatformPartnerSettlementStatus]] = field(default=None)
    """정산 상태
    """
    partner_ids: Optional[list[str]] = field(default=None)
    settlement_types: Optional[list[PlatformPartnerSettlementType]] = field(default=None)
    """정산 유형
    """
    keyword: Optional[PlatformPartnerSettlementFilterKeywordInput] = field(default=None)


def _serialize_platform_partner_settlement_filter_input(obj: PlatformPartnerSettlementFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.settlement_dates is not None:
        entity["settlementDates"] = obj.settlement_dates
    if obj.contract_ids is not None:
        entity["contractIds"] = obj.contract_ids
    if obj.partner_tags is not None:
        entity["partnerTags"] = obj.partner_tags
    if obj.settlement_currencies is not None:
        entity["settlementCurrencies"] = list(map(_serialize_currency, obj.settlement_currencies))
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_platform_partner_settlement_status, obj.statuses))
    if obj.partner_ids is not None:
        entity["partnerIds"] = obj.partner_ids
    if obj.settlement_types is not None:
        entity["settlementTypes"] = list(map(_serialize_platform_partner_settlement_type, obj.settlement_types))
    if obj.keyword is not None:
        entity["keyword"] = _serialize_platform_partner_settlement_filter_keyword_input(obj.keyword)
    return entity


def _deserialize_platform_partner_settlement_filter_input(obj: Any) -> PlatformPartnerSettlementFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "settlementDates" in obj:
        settlement_dates = obj["settlementDates"]
        if not isinstance(settlement_dates, list):
            raise ValueError(f"{repr(settlement_dates)} is not list")
        for i, item in enumerate(settlement_dates):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        settlement_dates = None
    if "contractIds" in obj:
        contract_ids = obj["contractIds"]
        if not isinstance(contract_ids, list):
            raise ValueError(f"{repr(contract_ids)} is not list")
        for i, item in enumerate(contract_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        contract_ids = None
    if "partnerTags" in obj:
        partner_tags = obj["partnerTags"]
        if not isinstance(partner_tags, list):
            raise ValueError(f"{repr(partner_tags)} is not list")
        for i, item in enumerate(partner_tags):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        partner_tags = None
    if "settlementCurrencies" in obj:
        settlement_currencies = obj["settlementCurrencies"]
        if not isinstance(settlement_currencies, list):
            raise ValueError(f"{repr(settlement_currencies)} is not list")
        for i, item in enumerate(settlement_currencies):
            item = _deserialize_currency(item)
            settlement_currencies[i] = item
    else:
        settlement_currencies = None
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_platform_partner_settlement_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "partnerIds" in obj:
        partner_ids = obj["partnerIds"]
        if not isinstance(partner_ids, list):
            raise ValueError(f"{repr(partner_ids)} is not list")
        for i, item in enumerate(partner_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        partner_ids = None
    if "settlementTypes" in obj:
        settlement_types = obj["settlementTypes"]
        if not isinstance(settlement_types, list):
            raise ValueError(f"{repr(settlement_types)} is not list")
        for i, item in enumerate(settlement_types):
            item = _deserialize_platform_partner_settlement_type(item)
            settlement_types[i] = item
    else:
        settlement_types = None
    if "keyword" in obj:
        keyword = obj["keyword"]
        keyword = _deserialize_platform_partner_settlement_filter_keyword_input(keyword)
    else:
        keyword = None
    return PlatformPartnerSettlementFilterInput(settlement_dates, contract_ids, partner_tags, settlement_currencies, statuses, partner_ids, settlement_types, keyword)
