from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ...platform.payout.platform_payout_account import PlatformPayoutAccount, _deserialize_platform_payout_account, _serialize_platform_payout_account
from ...platform.platform_payout_method import PlatformPayoutMethod, _deserialize_platform_payout_method, _serialize_platform_payout_method
from ...platform.payout.platform_payout_settlement_statement_summary import PlatformPayoutSettlementStatementSummary, _deserialize_platform_payout_settlement_statement_summary, _serialize_platform_payout_settlement_statement_summary
from ...platform.payout.platform_payout_status import PlatformPayoutStatus, _deserialize_platform_payout_status, _serialize_platform_payout_status
from ...platform.payout.platform_payout_tax_invoice_status import PlatformPayoutTaxInvoiceStatus, _deserialize_platform_payout_tax_invoice_status, _serialize_platform_payout_tax_invoice_status
from ...platform.settlement_amount_type import SettlementAmountType, _deserialize_settlement_amount_type, _serialize_settlement_amount_type

@dataclass
class PlatformPayout:
    id: str
    """지급 고유 아이디
    """
    graphql_id: str
    bulk_payout_id: str
    bulk_payout_graphql_id: str
    method: PlatformPayoutMethod
    status: PlatformPayoutStatus
    status_updated_at: str
    """(RFC 3339 date-time)
    """
    partner: PlatformPartner
    account: PlatformPayoutAccount
    tax_invoice_status: PlatformPayoutTaxInvoiceStatus
    """세금계산서 상태
    """
    currency: Currency
    amount: int
    """지급금액
    (int64)
    """
    supply_amount: int
    """공급가액
    (int64)
    """
    tax_free_amount: int
    """면세 금액
    (int64)
    """
    vat_amount: int
    """부가세
    (int64)
    """
    settlement_amount: int
    """정산 금액
    (int64)
    """
    settlement_tax_free_amount: int
    """정산 면세 금액
    (int64)
    """
    income_tax_amount: int
    """원천징수세액 (소득세)
    (int64)
    """
    local_income_tax_amount: int
    """원천징수세액 (지방소득세)
    (int64)
    """
    created_at: str
    """(RFC 3339 date-time)
    """
    deduct_wht: bool
    """지급 금액에서 원천징수세 차감 여부
    """
    settlement_amount_type: SettlementAmountType
    """정산 금액 취급 기준
    """
    settlement_statement: PlatformPayoutSettlementStatementSummary
    """정산 내역서 요약 정보
    """
    memo: Optional[str] = field(default=None)
    tax_invoice_id: Optional[str] = field(default=None)
    """세금계산서 아이디
    """
    withdrawal_memo: Optional[str] = field(default=None)
    deposit_memo: Optional[str] = field(default=None)
    scheduled_at: Optional[str] = field(default=None)
    """(RFC 3339 date-time)
    """
    fail_reason: Optional[str] = field(default=None)
    """실패 사유
    """


def _serialize_platform_payout(obj: PlatformPayout) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["bulkPayoutId"] = obj.bulk_payout_id
    entity["bulkPayoutGraphqlId"] = obj.bulk_payout_graphql_id
    entity["method"] = _serialize_platform_payout_method(obj.method)
    entity["status"] = _serialize_platform_payout_status(obj.status)
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["partner"] = _serialize_platform_partner(obj.partner)
    entity["account"] = _serialize_platform_payout_account(obj.account)
    entity["taxInvoiceStatus"] = _serialize_platform_payout_tax_invoice_status(obj.tax_invoice_status)
    entity["currency"] = _serialize_currency(obj.currency)
    entity["amount"] = obj.amount
    entity["supplyAmount"] = obj.supply_amount
    entity["taxFreeAmount"] = obj.tax_free_amount
    entity["vatAmount"] = obj.vat_amount
    entity["settlementAmount"] = obj.settlement_amount
    entity["settlementTaxFreeAmount"] = obj.settlement_tax_free_amount
    entity["incomeTaxAmount"] = obj.income_tax_amount
    entity["localIncomeTaxAmount"] = obj.local_income_tax_amount
    entity["createdAt"] = obj.created_at
    entity["deductWht"] = obj.deduct_wht
    entity["settlementAmountType"] = _serialize_settlement_amount_type(obj.settlement_amount_type)
    entity["settlementStatement"] = _serialize_platform_payout_settlement_statement_summary(obj.settlement_statement)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.tax_invoice_id is not None:
        entity["taxInvoiceId"] = obj.tax_invoice_id
    if obj.withdrawal_memo is not None:
        entity["withdrawalMemo"] = obj.withdrawal_memo
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
    if obj.scheduled_at is not None:
        entity["scheduledAt"] = obj.scheduled_at
    if obj.fail_reason is not None:
        entity["failReason"] = obj.fail_reason
    return entity


def _deserialize_platform_payout(obj: Any) -> PlatformPayout:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
    if "bulkPayoutId" not in obj:
        raise KeyError(f"'bulkPayoutId' is not in {obj}")
    bulk_payout_id = obj["bulkPayoutId"]
    if not isinstance(bulk_payout_id, str):
        raise ValueError(f"{repr(bulk_payout_id)} is not str")
    if "bulkPayoutGraphqlId" not in obj:
        raise KeyError(f"'bulkPayoutGraphqlId' is not in {obj}")
    bulk_payout_graphql_id = obj["bulkPayoutGraphqlId"]
    if not isinstance(bulk_payout_graphql_id, str):
        raise ValueError(f"{repr(bulk_payout_graphql_id)} is not str")
    if "method" not in obj:
        raise KeyError(f"'method' is not in {obj}")
    method = obj["method"]
    method = _deserialize_platform_payout_method(method)
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_payout_status(status)
    if "statusUpdatedAt" not in obj:
        raise KeyError(f"'statusUpdatedAt' is not in {obj}")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError(f"{repr(status_updated_at)} is not str")
    if "partner" not in obj:
        raise KeyError(f"'partner' is not in {obj}")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    if "account" not in obj:
        raise KeyError(f"'account' is not in {obj}")
    account = obj["account"]
    account = _deserialize_platform_payout_account(account)
    if "taxInvoiceStatus" not in obj:
        raise KeyError(f"'taxInvoiceStatus' is not in {obj}")
    tax_invoice_status = obj["taxInvoiceStatus"]
    tax_invoice_status = _deserialize_platform_payout_tax_invoice_status(tax_invoice_status)
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "supplyAmount" not in obj:
        raise KeyError(f"'supplyAmount' is not in {obj}")
    supply_amount = obj["supplyAmount"]
    if not isinstance(supply_amount, int):
        raise ValueError(f"{repr(supply_amount)} is not int")
    if "taxFreeAmount" not in obj:
        raise KeyError(f"'taxFreeAmount' is not in {obj}")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError(f"{repr(tax_free_amount)} is not int")
    if "vatAmount" not in obj:
        raise KeyError(f"'vatAmount' is not in {obj}")
    vat_amount = obj["vatAmount"]
    if not isinstance(vat_amount, int):
        raise ValueError(f"{repr(vat_amount)} is not int")
    if "settlementAmount" not in obj:
        raise KeyError(f"'settlementAmount' is not in {obj}")
    settlement_amount = obj["settlementAmount"]
    if not isinstance(settlement_amount, int):
        raise ValueError(f"{repr(settlement_amount)} is not int")
    if "settlementTaxFreeAmount" not in obj:
        raise KeyError(f"'settlementTaxFreeAmount' is not in {obj}")
    settlement_tax_free_amount = obj["settlementTaxFreeAmount"]
    if not isinstance(settlement_tax_free_amount, int):
        raise ValueError(f"{repr(settlement_tax_free_amount)} is not int")
    if "incomeTaxAmount" not in obj:
        raise KeyError(f"'incomeTaxAmount' is not in {obj}")
    income_tax_amount = obj["incomeTaxAmount"]
    if not isinstance(income_tax_amount, int):
        raise ValueError(f"{repr(income_tax_amount)} is not int")
    if "localIncomeTaxAmount" not in obj:
        raise KeyError(f"'localIncomeTaxAmount' is not in {obj}")
    local_income_tax_amount = obj["localIncomeTaxAmount"]
    if not isinstance(local_income_tax_amount, int):
        raise ValueError(f"{repr(local_income_tax_amount)} is not int")
    if "createdAt" not in obj:
        raise KeyError(f"'createdAt' is not in {obj}")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError(f"{repr(created_at)} is not str")
    if "deductWht" not in obj:
        raise KeyError(f"'deductWht' is not in {obj}")
    deduct_wht = obj["deductWht"]
    if not isinstance(deduct_wht, bool):
        raise ValueError(f"{repr(deduct_wht)} is not bool")
    if "settlementAmountType" not in obj:
        raise KeyError(f"'settlementAmountType' is not in {obj}")
    settlement_amount_type = obj["settlementAmountType"]
    settlement_amount_type = _deserialize_settlement_amount_type(settlement_amount_type)
    if "settlementStatement" not in obj:
        raise KeyError(f"'settlementStatement' is not in {obj}")
    settlement_statement = obj["settlementStatement"]
    settlement_statement = _deserialize_platform_payout_settlement_statement_summary(settlement_statement)
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "taxInvoiceId" in obj:
        tax_invoice_id = obj["taxInvoiceId"]
        if not isinstance(tax_invoice_id, str):
            raise ValueError(f"{repr(tax_invoice_id)} is not str")
    else:
        tax_invoice_id = None
    if "withdrawalMemo" in obj:
        withdrawal_memo = obj["withdrawalMemo"]
        if not isinstance(withdrawal_memo, str):
            raise ValueError(f"{repr(withdrawal_memo)} is not str")
    else:
        withdrawal_memo = None
    if "depositMemo" in obj:
        deposit_memo = obj["depositMemo"]
        if not isinstance(deposit_memo, str):
            raise ValueError(f"{repr(deposit_memo)} is not str")
    else:
        deposit_memo = None
    if "scheduledAt" in obj:
        scheduled_at = obj["scheduledAt"]
        if not isinstance(scheduled_at, str):
            raise ValueError(f"{repr(scheduled_at)} is not str")
    else:
        scheduled_at = None
    if "failReason" in obj:
        fail_reason = obj["failReason"]
        if not isinstance(fail_reason, str):
            raise ValueError(f"{repr(fail_reason)} is not str")
    else:
        fail_reason = None
    return PlatformPayout(id, graphql_id, bulk_payout_id, bulk_payout_graphql_id, method, status, status_updated_at, partner, account, tax_invoice_status, currency, amount, supply_amount, tax_free_amount, vat_amount, settlement_amount, settlement_tax_free_amount, income_tax_amount, local_income_tax_amount, created_at, deduct_wht, settlement_amount_type, settlement_statement, memo, tax_invoice_id, withdrawal_memo, deposit_memo, scheduled_at, fail_reason)
