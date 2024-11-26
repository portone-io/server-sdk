from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.bank import Bank, _deserialize_bank, _serialize_bank
from ...common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class PlatformPartnerPayoutAccountTransfer:
    """계좌 이체 유형
    """
    id: str
    """계좌 이체 아이디
    """
    sequence_number: int
    """거래 일련번호
    (int32)
    """
    currency: Currency
    """통화
    """
    deposit_bank: Bank
    """입금 계좌 은행
    """
    deposit_account_number: str
    """입금 계좌 번호
    """
    amount: int
    """금액
    (int64)
    """
    is_for_test: bool
    created_at: str
    """생성 일자
    (RFC 3339 date-time)
    """
    updated_at: str
    """수정 일자
    (RFC 3339 date-time)
    """
    partner_id: str
    """파트너 고유 아이디
    """
    partner_graphql_id: str
    bulk_payout_id: str
    """일괄 지급 고유 아이디
    """
    bulk_payout_graphql_id: str
    payout_id: str
    """지급 고유 아이디
    """
    payout_graphql_id: str
    withdrawal_memo: Optional[str] = field(default=None)
    """출금 계좌 적요
    """
    deposit_memo: Optional[str] = field(default=None)
    """입금 계좌 적요
    """
    balance: Optional[int] = field(default=None)
    """잔액
    (int64)
    """
    fail_reason: Optional[str] = field(default=None)
    """실패 사유
    """


def _serialize_platform_partner_payout_account_transfer(obj: PlatformPartnerPayoutAccountTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PARTNER_PAYOUT"
    entity["id"] = obj.id
    entity["sequenceNumber"] = obj.sequence_number
    entity["currency"] = _serialize_currency(obj.currency)
    entity["depositBank"] = _serialize_bank(obj.deposit_bank)
    entity["depositAccountNumber"] = obj.deposit_account_number
    entity["amount"] = obj.amount
    entity["isForTest"] = obj.is_for_test
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    entity["partnerId"] = obj.partner_id
    entity["partnerGraphqlId"] = obj.partner_graphql_id
    entity["bulkPayoutId"] = obj.bulk_payout_id
    entity["bulkPayoutGraphqlId"] = obj.bulk_payout_graphql_id
    entity["payoutId"] = obj.payout_id
    entity["payoutGraphqlId"] = obj.payout_graphql_id
    if obj.withdrawal_memo is not None:
        entity["withdrawalMemo"] = obj.withdrawal_memo
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
    if obj.balance is not None:
        entity["balance"] = obj.balance
    if obj.fail_reason is not None:
        entity["failReason"] = obj.fail_reason
    return entity


def _deserialize_platform_partner_payout_account_transfer(obj: Any) -> PlatformPartnerPayoutAccountTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PARTNER_PAYOUT":
        raise ValueError(f"{repr(type)} is not 'PARTNER_PAYOUT'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "sequenceNumber" not in obj:
        raise KeyError(f"'sequenceNumber' is not in {obj}")
    sequence_number = obj["sequenceNumber"]
    if not isinstance(sequence_number, int):
        raise ValueError(f"{repr(sequence_number)} is not int")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "depositBank" not in obj:
        raise KeyError(f"'depositBank' is not in {obj}")
    deposit_bank = obj["depositBank"]
    deposit_bank = _deserialize_bank(deposit_bank)
    if "depositAccountNumber" not in obj:
        raise KeyError(f"'depositAccountNumber' is not in {obj}")
    deposit_account_number = obj["depositAccountNumber"]
    if not isinstance(deposit_account_number, str):
        raise ValueError(f"{repr(deposit_account_number)} is not str")
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "createdAt" not in obj:
        raise KeyError(f"'createdAt' is not in {obj}")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError(f"{repr(created_at)} is not str")
    if "updatedAt" not in obj:
        raise KeyError(f"'updatedAt' is not in {obj}")
    updated_at = obj["updatedAt"]
    if not isinstance(updated_at, str):
        raise ValueError(f"{repr(updated_at)} is not str")
    if "partnerId" not in obj:
        raise KeyError(f"'partnerId' is not in {obj}")
    partner_id = obj["partnerId"]
    if not isinstance(partner_id, str):
        raise ValueError(f"{repr(partner_id)} is not str")
    if "partnerGraphqlId" not in obj:
        raise KeyError(f"'partnerGraphqlId' is not in {obj}")
    partner_graphql_id = obj["partnerGraphqlId"]
    if not isinstance(partner_graphql_id, str):
        raise ValueError(f"{repr(partner_graphql_id)} is not str")
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
    if "payoutId" not in obj:
        raise KeyError(f"'payoutId' is not in {obj}")
    payout_id = obj["payoutId"]
    if not isinstance(payout_id, str):
        raise ValueError(f"{repr(payout_id)} is not str")
    if "payoutGraphqlId" not in obj:
        raise KeyError(f"'payoutGraphqlId' is not in {obj}")
    payout_graphql_id = obj["payoutGraphqlId"]
    if not isinstance(payout_graphql_id, str):
        raise ValueError(f"{repr(payout_graphql_id)} is not str")
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
    if "balance" in obj:
        balance = obj["balance"]
        if not isinstance(balance, int):
            raise ValueError(f"{repr(balance)} is not int")
    else:
        balance = None
    if "failReason" in obj:
        fail_reason = obj["failReason"]
        if not isinstance(fail_reason, str):
            raise ValueError(f"{repr(fail_reason)} is not str")
    else:
        fail_reason = None
    return PlatformPartnerPayoutAccountTransfer(id, sequence_number, currency, deposit_bank, deposit_account_number, amount, is_for_test, created_at, updated_at, partner_id, partner_graphql_id, bulk_payout_id, bulk_payout_graphql_id, payout_id, payout_graphql_id, withdrawal_memo, deposit_memo, balance, fail_reason)
