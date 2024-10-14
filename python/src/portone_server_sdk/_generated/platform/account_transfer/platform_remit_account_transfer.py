from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class PlatformRemitAccountTransfer:
    type: Literal["REMIT"] = field(repr=False)
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
    document_id: str
    """전자서명 아이디
    """
    withdrawal_memo: Optional[str]
    """출금 계좌 적요
    """
    deposit_memo: Optional[str]
    """입금 계좌 적요
    """
    balance: Optional[int]
    """잔액
    (int64)
    """
    fail_reason: Optional[str]
    """실패 사유
    """


def _serialize_platform_remit_account_transfer(obj: PlatformRemitAccountTransfer) -> Any:
    entity = {}
    entity["type"] = "REMIT"
    entity["id"] = obj.id
    entity["sequenceNumber"] = obj.sequence_number
    entity["currency"] = _serialize_currency(obj.currency)
    entity["depositBank"] = _serialize_bank(obj.deposit_bank)
    entity["depositAccountNumber"] = obj.deposit_account_number
    entity["amount"] = obj.amount
    entity["isForTest"] = obj.is_for_test
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    entity["documentId"] = obj.document_id
    if obj.withdrawal_memo is not None:
        entity["withdrawalMemo"] = obj.withdrawal_memo
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
    if obj.balance is not None:
        entity["balance"] = obj.balance
    if obj.fail_reason is not None:
        entity["failReason"] = obj.fail_reason
    return entity


def _deserialize_platform_remit_account_transfer(obj: Any) -> PlatformRemitAccountTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "REMIT":
        raise ValueError(f"{repr(type)} is not 'REMIT'")
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
    if "documentId" not in obj:
        raise KeyError(f"'documentId' is not in {obj}")
    document_id = obj["documentId"]
    if not isinstance(document_id, str):
        raise ValueError(f"{repr(document_id)} is not str")
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
    return PlatformRemitAccountTransfer(type, id, sequence_number, currency, deposit_bank, deposit_account_number, amount, is_for_test, created_at, updated_at, document_id, withdrawal_memo, deposit_memo, balance, fail_reason)
