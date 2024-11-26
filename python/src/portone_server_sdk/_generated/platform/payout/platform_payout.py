from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from ...platform.payout.platform_payout_account import PlatformPayoutAccount, _deserialize_platform_payout_account, _serialize_platform_payout_account
from ...platform.platform_payout_method import PlatformPayoutMethod, _deserialize_platform_payout_method, _serialize_platform_payout_method
from ...platform.payout.platform_payout_status import PlatformPayoutStatus, _deserialize_platform_payout_status, _serialize_platform_payout_status

@dataclass
class PlatformPayout:
    id: str
    """지급 고유 아이디
    """
    graphql_id: str
    method: PlatformPayoutMethod
    status: PlatformPayoutStatus
    status_updated_at: str
    """(RFC 3339 date-time)
    """
    partner: PlatformPartner
    account: PlatformPayoutAccount
    currency: Currency
    amount: int
    """(int64)
    """
    settlement_amount: int
    """(int64)
    """
    income_tax_amount: int
    """(int64)
    """
    local_income_tax_amount: int
    """(int64)
    """
    created_at: str
    """(RFC 3339 date-time)
    """
    memo: Optional[str] = field(default=None)
    withdrawal_memo: Optional[str] = field(default=None)
    deposit_memo: Optional[str] = field(default=None)
    scheduled_at: Optional[str] = field(default=None)
    """(RFC 3339 date-time)
    """


def _serialize_platform_payout(obj: PlatformPayout) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["method"] = _serialize_platform_payout_method(obj.method)
    entity["status"] = _serialize_platform_payout_status(obj.status)
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["partner"] = _serialize_platform_partner(obj.partner)
    entity["account"] = _serialize_platform_payout_account(obj.account)
    entity["currency"] = _serialize_currency(obj.currency)
    entity["amount"] = obj.amount
    entity["settlementAmount"] = obj.settlement_amount
    entity["incomeTaxAmount"] = obj.income_tax_amount
    entity["localIncomeTaxAmount"] = obj.local_income_tax_amount
    entity["createdAt"] = obj.created_at
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.withdrawal_memo is not None:
        entity["withdrawalMemo"] = obj.withdrawal_memo
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
    if obj.scheduled_at is not None:
        entity["scheduledAt"] = obj.scheduled_at
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
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "settlementAmount" not in obj:
        raise KeyError(f"'settlementAmount' is not in {obj}")
    settlement_amount = obj["settlementAmount"]
    if not isinstance(settlement_amount, int):
        raise ValueError(f"{repr(settlement_amount)} is not int")
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
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
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
    return PlatformPayout(id, graphql_id, method, status, status_updated_at, partner, account, currency, amount, settlement_amount, income_tax_amount, local_income_tax_amount, created_at, memo, withdrawal_memo, deposit_memo, scheduled_at)
