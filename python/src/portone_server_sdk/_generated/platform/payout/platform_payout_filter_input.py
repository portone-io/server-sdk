from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.bank import Bank, _deserialize_bank, _serialize_bank
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.platform_partner_taxation_type import PlatformPartnerTaxationType, _deserialize_platform_partner_taxation_type, _serialize_platform_partner_taxation_type
from ...platform.platform_partner_type_name import PlatformPartnerTypeName, _deserialize_platform_partner_type_name, _serialize_platform_partner_type_name
from ...platform.payout.platform_payout_filter_input_criteria import PlatformPayoutFilterInputCriteria, _deserialize_platform_payout_filter_input_criteria, _serialize_platform_payout_filter_input_criteria
from ...platform.payout.platform_payout_settlement_statement_status import PlatformPayoutSettlementStatementStatus, _deserialize_platform_payout_settlement_statement_status, _serialize_platform_payout_settlement_statement_status
from ...platform.payout.platform_payout_status import PlatformPayoutStatus, _deserialize_platform_payout_status, _serialize_platform_payout_status
from ...platform.payout.platform_payout_tax_invoice_status import PlatformPayoutTaxInvoiceStatus, _deserialize_platform_payout_tax_invoice_status, _serialize_platform_payout_tax_invoice_status

@dataclass
class PlatformPayoutFilterInput:
    """지급 내역 필터 입력 정보
    """
    criteria: PlatformPayoutFilterInputCriteria
    """조회 기준
    """
    statuses: Optional[list[PlatformPayoutStatus]] = field(default=None)
    """지급 상태

    값이 존재하는 경우 해당 리스트에 포함되는 지급 상태를 가진 지급 내역을 조회합니다.
    """
    partner_ids: Optional[list[str]] = field(default=None)
    """파트너 아이디

    값이 존재하는 경우 해당 리스트에 포함되는 파트너 아이디를 가진 지급 내역을 조회합니다.
    """
    payout_account_banks: Optional[list[Bank]] = field(default=None)
    """지급 계좌 은행

    값이 존재하는 경우 해당 리스트에 포함되는 지급 계좌 은행을 가진 지급 내역을 조회합니다.
    """
    partner_tags: Optional[list[str]] = field(default=None)
    """파트너 태그

    값이 존재하는 경우 해당 리스트에 포함되는 파트너 태그를 하나 이상 가진 지급 내역을 조회합니다.
    """
    payout_currencies: Optional[list[Currency]] = field(default=None)
    """지급 통화

    값이 존재하는 경우 해당 리스트에 포함되는 지급 통화를 가진 지급 내역을 조회합니다.
    """
    payout_ids: Optional[list[str]] = field(default=None)
    """지급 아이디

    값이 존재하는 경우 해당 리스트에 포함되는 지급 아이디를 가진 지급 내역을 조회합니다.
    """
    tax_invoice_statuses: Optional[list[PlatformPayoutTaxInvoiceStatus]] = field(default=None)
    """세금계산서 상태

    값이 존재하는 경우 해당 리스트에 포함되는 세금계산서 상태를 가진 지급 내역을 조회합니다.
    """
    partner_types: Optional[list[PlatformPartnerTypeName]] = field(default=None)
    """파트너 유형

    값이 존재하는 경우 해당 리스트에 포함되는 파트너 유형을 가진 지급 내역을 조회합니다.
    """
    partner_taxation_types: Optional[list[PlatformPartnerTaxationType]] = field(default=None)
    """파트너 과세 유형

    값이 존재하는 경우 해당 리스트에 포함되는 파트너 과세 유형을 가진 지급 내역을 조회합니다.
    """
    settlement_statement_statuses: Optional[list[PlatformPayoutSettlementStatementStatus]] = field(default=None)
    """정산 내역서 상태

    값이 존재하는 경우 해당 리스트에 포함되는 정산 내역서 상태를 가진 지급 내역을 조회합니다.
    """


def _serialize_platform_payout_filter_input(obj: PlatformPayoutFilterInput) -> Any:
    if isinstance(obj, dict):
        return obj
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
    if obj.payout_ids is not None:
        entity["payoutIds"] = obj.payout_ids
    if obj.tax_invoice_statuses is not None:
        entity["taxInvoiceStatuses"] = list(map(_serialize_platform_payout_tax_invoice_status, obj.tax_invoice_statuses))
    if obj.partner_types is not None:
        entity["partnerTypes"] = list(map(_serialize_platform_partner_type_name, obj.partner_types))
    if obj.partner_taxation_types is not None:
        entity["partnerTaxationTypes"] = list(map(_serialize_platform_partner_taxation_type, obj.partner_taxation_types))
    if obj.settlement_statement_statuses is not None:
        entity["settlementStatementStatuses"] = list(map(_serialize_platform_payout_settlement_statement_status, obj.settlement_statement_statuses))
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
    if "payoutIds" in obj:
        payout_ids = obj["payoutIds"]
        if not isinstance(payout_ids, list):
            raise ValueError(f"{repr(payout_ids)} is not list")
        for i, item in enumerate(payout_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        payout_ids = None
    if "taxInvoiceStatuses" in obj:
        tax_invoice_statuses = obj["taxInvoiceStatuses"]
        if not isinstance(tax_invoice_statuses, list):
            raise ValueError(f"{repr(tax_invoice_statuses)} is not list")
        for i, item in enumerate(tax_invoice_statuses):
            item = _deserialize_platform_payout_tax_invoice_status(item)
            tax_invoice_statuses[i] = item
    else:
        tax_invoice_statuses = None
    if "partnerTypes" in obj:
        partner_types = obj["partnerTypes"]
        if not isinstance(partner_types, list):
            raise ValueError(f"{repr(partner_types)} is not list")
        for i, item in enumerate(partner_types):
            item = _deserialize_platform_partner_type_name(item)
            partner_types[i] = item
    else:
        partner_types = None
    if "partnerTaxationTypes" in obj:
        partner_taxation_types = obj["partnerTaxationTypes"]
        if not isinstance(partner_taxation_types, list):
            raise ValueError(f"{repr(partner_taxation_types)} is not list")
        for i, item in enumerate(partner_taxation_types):
            item = _deserialize_platform_partner_taxation_type(item)
            partner_taxation_types[i] = item
    else:
        partner_taxation_types = None
    if "settlementStatementStatuses" in obj:
        settlement_statement_statuses = obj["settlementStatementStatuses"]
        if not isinstance(settlement_statement_statuses, list):
            raise ValueError(f"{repr(settlement_statement_statuses)} is not list")
        for i, item in enumerate(settlement_statement_statuses):
            item = _deserialize_platform_payout_settlement_statement_status(item)
            settlement_statement_statuses[i] = item
    else:
        settlement_statement_statuses = None
    return PlatformPayoutFilterInput(criteria, statuses, partner_ids, payout_account_banks, partner_tags, payout_currencies, payout_ids, tax_invoice_statuses, partner_types, partner_taxation_types, settlement_statement_statuses)
