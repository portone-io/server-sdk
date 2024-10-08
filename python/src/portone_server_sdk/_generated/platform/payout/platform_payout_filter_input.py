from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.platform.payout.platform_payout_filter_input_criteria import PlatformPayoutFilterInputCriteria, _deserialize_platform_payout_filter_input_criteria, _serialize_platform_payout_filter_input_criteria
from portone_server_sdk._generated.platform.payout.platform_payout_status import PlatformPayoutStatus, _deserialize_platform_payout_status, _serialize_platform_payout_status

@dataclass
class PlatformPayoutFilterInput:
    criteria: PlatformPayoutFilterInputCriteria
    statuses: Optional[list[PlatformPayoutStatus]]
    partner_ids: Optional[list[str]]
    payout_account_banks: Optional[list[Bank]]
    """은행
    """
    partner_tags: Optional[list[str]]
    payout_currencies: Optional[list[Currency]]
    """통화 단위
    """


def _serialize_platform_payout_filter_input(obj: PlatformPayoutFilterInput) -> Any:
    entity = {}
    entity["criteria"] = _serialize_platform_payout_filter_input_criteria(obj.criteria)
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_platform_payout_status, obj.statuses))
    if obj.partner_ids is not None:
        entity["partnerIds"] = obj.partner_ids
    if obj.payout_account_banks is not None:
        entity["payoutAccountBanks"] = list(map(_serialize_bank, obj.payout_account_banks))
    if obj.partner_tags is not None:
        entity["partnerTags"] = obj.partner_tags
    if obj.payout_currencies is not None:
        entity["payoutCurrencies"] = list(map(_serialize_currency, obj.payout_currencies))
    return entity


def _deserialize_platform_payout_filter_input(obj: Any) -> PlatformPayoutFilterInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "criteria" not in obj:
        raise KeyError(f"'criteria' is not in {obj}")
    criteria = obj["criteria"]
    criteria = _deserialize_platform_payout_filter_input_criteria(criteria)
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_platform_payout_status(item)
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
    if "payoutAccountBanks" in obj:
        payout_account_banks = obj["payoutAccountBanks"]
        if not isinstance(payout_account_banks, list):
            raise ValueError(f"{repr(payout_account_banks)} is not list")
        for i, item in enumerate(payout_account_banks):
            item = _deserialize_bank(item)
            payout_account_banks[i] = item
    else:
        payout_account_banks = None
    if "partnerTags" in obj:
        partner_tags = obj["partnerTags"]
        if not isinstance(partner_tags, list):
            raise ValueError(f"{repr(partner_tags)} is not list")
        for i, item in enumerate(partner_tags):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        partner_tags = None
    if "payoutCurrencies" in obj:
        payout_currencies = obj["payoutCurrencies"]
        if not isinstance(payout_currencies, list):
            raise ValueError(f"{repr(payout_currencies)} is not list")
        for i, item in enumerate(payout_currencies):
            item = _deserialize_currency(item)
            payout_currencies[i] = item
    else:
        payout_currencies = None
    return PlatformPayoutFilterInput(criteria, statuses, partner_ids, payout_account_banks, partner_tags, payout_currencies)
