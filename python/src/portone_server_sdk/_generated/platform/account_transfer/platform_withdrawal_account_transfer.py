from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.bank import Bank, _deserialize_bank, _serialize_bank
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.account_transfer.platform_account_transfer_status import PlatformAccountTransferStatus, _deserialize_platform_account_transfer_status, _serialize_platform_account_transfer_status
from ...platform.account_transfer.type import Type, _deserialize_type, _serialize_type

@dataclass
class PlatformWithdrawalAccountTransfer:
    """계좌 이체 유형
    """
    id: str
    """계좌 이체 아이디
    """
    bank_account_id: str
    """출금 계좌 아이디
    """
    bank_account_graphql_id: str
    currency: Currency
    """통화
    """
    deposit_bank: Bank
    """이체 계좌 은행
    """
    deposit_account_number: str
    """이체 계좌 번호
    """
    deposit_account_holder: str
    """예금주
    """
    amount: int
    """금액
    (int64)
    """
    created_at: str
    """생성 일시
    (RFC 3339 date-time)
    """
    updated_at: str
    """수정 일시
    (RFC 3339 date-time)
    """
    is_for_test: bool
    """테스트 모드 여부
    """
    withdrawal_type: Type
    """출금 유형
    """
    status_updated_at: str
    """상태 업데이트 일시
    (RFC 3339 date-time)
    """
    status: PlatformAccountTransferStatus
    """상태
    """
    sequence_number: Optional[int] = field(default=None)
    """거래 일련번호
    (int32)
    """
    withdrawal_memo: Optional[str] = field(default=None)
    """보내는 이 통장 메모
    """
    deposit_memo: Optional[str] = field(default=None)
    """받는 이 통장 메모
    """
    balance: Optional[int] = field(default=None)
    """잔액
    (int64)
    """
    fail_reason: Optional[str] = field(default=None)
    """실패 사유
    """
    traded_at: Optional[str] = field(default=None)
    """이체 일시
    (RFC 3339 date-time)
    """
    partner_id: Optional[str] = field(default=None)
    """파트너 고유 아이디
    """
    partner_graphql_id: Optional[str] = field(default=None)
    bulk_payout_id: Optional[str] = field(default=None)
    """일괄 지급 고유 아이디
    """
    bulk_payout_graphql_id: Optional[str] = field(default=None)
    payout_id: Optional[str] = field(default=None)
    """지급 고유 아이디
    """
    payout_graphql_id: Optional[str] = field(default=None)
    bulk_account_transfer_id: Optional[str] = field(default=None)
    bulk_account_transfer_graphql_id: Optional[str] = field(default=None)
    document_id: Optional[str] = field(default=None)
    """전자서명 아이디
    """
    scheduled_at: Optional[str] = field(default=None)
    """예정 일시
    (RFC 3339 date-time)
    """


def _serialize_platform_withdrawal_account_transfer(obj: PlatformWithdrawalAccountTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "WITHDRAWAL"
    entity["id"] = obj.id
    entity["bankAccountId"] = obj.bank_account_id
    entity["bankAccountGraphqlId"] = obj.bank_account_graphql_id
    entity["currency"] = _serialize_currency(obj.currency)
    entity["depositBank"] = _serialize_bank(obj.deposit_bank)
    entity["depositAccountNumber"] = obj.deposit_account_number
    entity["depositAccountHolder"] = obj.deposit_account_holder
    entity["amount"] = obj.amount
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    entity["isForTest"] = obj.is_for_test
    entity["withdrawalType"] = _serialize_type(obj.withdrawal_type)
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["status"] = _serialize_platform_account_transfer_status(obj.status)
    if obj.sequence_number is not None:
        entity["sequenceNumber"] = obj.sequence_number
    if obj.withdrawal_memo is not None:
        entity["withdrawalMemo"] = obj.withdrawal_memo
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
    if obj.balance is not None:
        entity["balance"] = obj.balance
    if obj.fail_reason is not None:
        entity["failReason"] = obj.fail_reason
    if obj.traded_at is not None:
        entity["tradedAt"] = obj.traded_at
    if obj.partner_id is not None:
        entity["partnerId"] = obj.partner_id
    if obj.partner_graphql_id is not None:
        entity["partnerGraphqlId"] = obj.partner_graphql_id
    if obj.bulk_payout_id is not None:
        entity["bulkPayoutId"] = obj.bulk_payout_id
    if obj.bulk_payout_graphql_id is not None:
        entity["bulkPayoutGraphqlId"] = obj.bulk_payout_graphql_id
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    if obj.payout_graphql_id is not None:
        entity["payoutGraphqlId"] = obj.payout_graphql_id
    if obj.bulk_account_transfer_id is not None:
        entity["bulkAccountTransferId"] = obj.bulk_account_transfer_id
    if obj.bulk_account_transfer_graphql_id is not None:
        entity["bulkAccountTransferGraphqlId"] = obj.bulk_account_transfer_graphql_id
    if obj.document_id is not None:
        entity["documentId"] = obj.document_id
    if obj.scheduled_at is not None:
        entity["scheduledAt"] = obj.scheduled_at
    return entity


def _deserialize_platform_withdrawal_account_transfer(obj: Any) -> PlatformWithdrawalAccountTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "WITHDRAWAL":
        raise ValueError(f"{repr(type)} is not 'WITHDRAWAL'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "bankAccountId" not in obj:
        raise KeyError(f"'bankAccountId' is not in {obj}")
    bank_account_id = obj["bankAccountId"]
    if not isinstance(bank_account_id, str):
        raise ValueError(f"{repr(bank_account_id)} is not str")
    if "bankAccountGraphqlId" not in obj:
        raise KeyError(f"'bankAccountGraphqlId' is not in {obj}")
    bank_account_graphql_id = obj["bankAccountGraphqlId"]
    if not isinstance(bank_account_graphql_id, str):
        raise ValueError(f"{repr(bank_account_graphql_id)} is not str")
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
    if "depositAccountHolder" not in obj:
        raise KeyError(f"'depositAccountHolder' is not in {obj}")
    deposit_account_holder = obj["depositAccountHolder"]
    if not isinstance(deposit_account_holder, str):
        raise ValueError(f"{repr(deposit_account_holder)} is not str")
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
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
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "withdrawalType" not in obj:
        raise KeyError(f"'withdrawalType' is not in {obj}")
    withdrawal_type = obj["withdrawalType"]
    withdrawal_type = _deserialize_type(withdrawal_type)
    if "statusUpdatedAt" not in obj:
        raise KeyError(f"'statusUpdatedAt' is not in {obj}")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError(f"{repr(status_updated_at)} is not str")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_account_transfer_status(status)
    if "sequenceNumber" in obj:
        sequence_number = obj["sequenceNumber"]
        if not isinstance(sequence_number, int):
            raise ValueError(f"{repr(sequence_number)} is not int")
    else:
        sequence_number = None
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
    if "tradedAt" in obj:
        traded_at = obj["tradedAt"]
        if not isinstance(traded_at, str):
            raise ValueError(f"{repr(traded_at)} is not str")
    else:
        traded_at = None
    if "partnerId" in obj:
        partner_id = obj["partnerId"]
        if not isinstance(partner_id, str):
            raise ValueError(f"{repr(partner_id)} is not str")
    else:
        partner_id = None
    if "partnerGraphqlId" in obj:
        partner_graphql_id = obj["partnerGraphqlId"]
        if not isinstance(partner_graphql_id, str):
            raise ValueError(f"{repr(partner_graphql_id)} is not str")
    else:
        partner_graphql_id = None
    if "bulkPayoutId" in obj:
        bulk_payout_id = obj["bulkPayoutId"]
        if not isinstance(bulk_payout_id, str):
            raise ValueError(f"{repr(bulk_payout_id)} is not str")
    else:
        bulk_payout_id = None
    if "bulkPayoutGraphqlId" in obj:
        bulk_payout_graphql_id = obj["bulkPayoutGraphqlId"]
        if not isinstance(bulk_payout_graphql_id, str):
            raise ValueError(f"{repr(bulk_payout_graphql_id)} is not str")
    else:
        bulk_payout_graphql_id = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError(f"{repr(payout_id)} is not str")
    else:
        payout_id = None
    if "payoutGraphqlId" in obj:
        payout_graphql_id = obj["payoutGraphqlId"]
        if not isinstance(payout_graphql_id, str):
            raise ValueError(f"{repr(payout_graphql_id)} is not str")
    else:
        payout_graphql_id = None
    if "bulkAccountTransferId" in obj:
        bulk_account_transfer_id = obj["bulkAccountTransferId"]
        if not isinstance(bulk_account_transfer_id, str):
            raise ValueError(f"{repr(bulk_account_transfer_id)} is not str")
    else:
        bulk_account_transfer_id = None
    if "bulkAccountTransferGraphqlId" in obj:
        bulk_account_transfer_graphql_id = obj["bulkAccountTransferGraphqlId"]
        if not isinstance(bulk_account_transfer_graphql_id, str):
            raise ValueError(f"{repr(bulk_account_transfer_graphql_id)} is not str")
    else:
        bulk_account_transfer_graphql_id = None
    if "documentId" in obj:
        document_id = obj["documentId"]
        if not isinstance(document_id, str):
            raise ValueError(f"{repr(document_id)} is not str")
    else:
        document_id = None
    if "scheduledAt" in obj:
        scheduled_at = obj["scheduledAt"]
        if not isinstance(scheduled_at, str):
            raise ValueError(f"{repr(scheduled_at)} is not str")
    else:
        scheduled_at = None
    return PlatformWithdrawalAccountTransfer(id, bank_account_id, bank_account_graphql_id, currency, deposit_bank, deposit_account_number, deposit_account_holder, amount, created_at, updated_at, is_for_test, withdrawal_type, status_updated_at, status, sequence_number, withdrawal_memo, deposit_memo, balance, fail_reason, traded_at, partner_id, partner_graphql_id, bulk_payout_id, bulk_payout_graphql_id, payout_id, payout_graphql_id, bulk_account_transfer_id, bulk_account_transfer_graphql_id, document_id, scheduled_at)
