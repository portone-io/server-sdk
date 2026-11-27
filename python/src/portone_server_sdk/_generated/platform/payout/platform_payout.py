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
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "graphqlId" not in obj:
        raise KeyError("Missing required field 'graphqlId'")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError("Expected str for graphql_id")
    if "bulkPayoutId" not in obj:
        raise KeyError("Missing required field 'bulkPayoutId'")
    bulk_payout_id = obj["bulkPayoutId"]
    if not isinstance(bulk_payout_id, str):
        raise ValueError("Expected str for bulk_payout_id")
    if "bulkPayoutGraphqlId" not in obj:
        raise KeyError("Missing required field 'bulkPayoutGraphqlId'")
    bulk_payout_graphql_id = obj["bulkPayoutGraphqlId"]
    if not isinstance(bulk_payout_graphql_id, str):
        raise ValueError("Expected str for bulk_payout_graphql_id")
    if "method" not in obj:
        raise KeyError("Missing required field 'method'")
    method = obj["method"]
    method = _deserialize_platform_payout_method(method)
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_platform_payout_status(status)
    if "statusUpdatedAt" not in obj:
        raise KeyError("Missing required field 'statusUpdatedAt'")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError("Expected str for status_updated_at")
    if "partner" not in obj:
        raise KeyError("Missing required field 'partner'")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    if "account" not in obj:
        raise KeyError("Missing required field 'account'")
    account = obj["account"]
    account = _deserialize_platform_payout_account(account)
    if "taxInvoiceStatus" not in obj:
        raise KeyError("Missing required field 'taxInvoiceStatus'")
    tax_invoice_status = obj["taxInvoiceStatus"]
    tax_invoice_status = _deserialize_platform_payout_tax_invoice_status(tax_invoice_status)
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError("Expected int for amount")
    if "supplyAmount" not in obj:
        raise KeyError("Missing required field 'supplyAmount'")
    supply_amount = obj["supplyAmount"]
    if not isinstance(supply_amount, int):
        raise ValueError("Expected int for supply_amount")
    if "taxFreeAmount" not in obj:
        raise KeyError("Missing required field 'taxFreeAmount'")
    tax_free_amount = obj["taxFreeAmount"]
    if not isinstance(tax_free_amount, int):
        raise ValueError("Expected int for tax_free_amount")
    if "vatAmount" not in obj:
        raise KeyError("Missing required field 'vatAmount'")
    vat_amount = obj["vatAmount"]
    if not isinstance(vat_amount, int):
        raise ValueError("Expected int for vat_amount")
    if "settlementAmount" not in obj:
        raise KeyError("Missing required field 'settlementAmount'")
    settlement_amount = obj["settlementAmount"]
    if not isinstance(settlement_amount, int):
        raise ValueError("Expected int for settlement_amount")
    if "settlementTaxFreeAmount" not in obj:
        raise KeyError("Missing required field 'settlementTaxFreeAmount'")
    settlement_tax_free_amount = obj["settlementTaxFreeAmount"]
    if not isinstance(settlement_tax_free_amount, int):
        raise ValueError("Expected int for settlement_tax_free_amount")
    if "incomeTaxAmount" not in obj:
        raise KeyError("Missing required field 'incomeTaxAmount'")
    income_tax_amount = obj["incomeTaxAmount"]
    if not isinstance(income_tax_amount, int):
        raise ValueError("Expected int for income_tax_amount")
    if "localIncomeTaxAmount" not in obj:
        raise KeyError("Missing required field 'localIncomeTaxAmount'")
    local_income_tax_amount = obj["localIncomeTaxAmount"]
    if not isinstance(local_income_tax_amount, int):
        raise ValueError("Expected int for local_income_tax_amount")
    if "createdAt" not in obj:
        raise KeyError("Missing required field 'createdAt'")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError("Expected str for created_at")
    if "deductWht" not in obj:
        raise KeyError("Missing required field 'deductWht'")
    deduct_wht = obj["deductWht"]
    if not isinstance(deduct_wht, bool):
        raise ValueError("Expected bool for deduct_wht")
    if "settlementAmountType" not in obj:
        raise KeyError("Missing required field 'settlementAmountType'")
    settlement_amount_type = obj["settlementAmountType"]
    settlement_amount_type = _deserialize_settlement_amount_type(settlement_amount_type)
    if "settlementStatement" not in obj:
        raise KeyError("Missing required field 'settlementStatement'")
    settlement_statement = obj["settlementStatement"]
    settlement_statement = _deserialize_platform_payout_settlement_statement_summary(settlement_statement)
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError("Expected str for memo")
    else:
        memo = None
    if "taxInvoiceId" in obj:
        tax_invoice_id = obj["taxInvoiceId"]
        if not isinstance(tax_invoice_id, str):
            raise ValueError("Expected str for tax_invoice_id")
    else:
        tax_invoice_id = None
    if "withdrawalMemo" in obj:
        withdrawal_memo = obj["withdrawalMemo"]
        if not isinstance(withdrawal_memo, str):
            raise ValueError("Expected str for withdrawal_memo")
    else:
        withdrawal_memo = None
    if "depositMemo" in obj:
        deposit_memo = obj["depositMemo"]
        if not isinstance(deposit_memo, str):
            raise ValueError("Expected str for deposit_memo")
    else:
        deposit_memo = None
    if "scheduledAt" in obj:
        scheduled_at = obj["scheduledAt"]
        if not isinstance(scheduled_at, str):
            raise ValueError("Expected str for scheduled_at")
    else:
        scheduled_at = None
    if "failReason" in obj:
        fail_reason = obj["failReason"]
        if not isinstance(fail_reason, str):
            raise ValueError("Expected str for fail_reason")
    else:
        fail_reason = None
    return PlatformPayout(id, graphql_id, bulk_payout_id, bulk_payout_graphql_id, method, status, status_updated_at, partner, account, tax_invoice_status, currency, amount, supply_amount, tax_free_amount, vat_amount, settlement_amount, settlement_tax_free_amount, income_tax_amount, local_income_tax_amount, created_at, deduct_wht, settlement_amount_type, settlement_statement, memo, tax_invoice_id, withdrawal_memo, deposit_memo, scheduled_at, fail_reason)
