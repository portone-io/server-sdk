from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.account_transfer.platform_account_transfer_status import PlatformAccountTransferStatus, _deserialize_platform_account_transfer_status, _serialize_platform_account_transfer_status
from ...platform.account_transfer.platform_bank_account_detail import PlatformBankAccountDetail, _deserialize_platform_bank_account_detail, _serialize_platform_bank_account_detail

@dataclass
class PlatformDepositAccountTransfer:
    """계좌 이체 유형
    """
    id: str
    """계좌 이체 아이디
    """
    bank_account_id: str
    """입금 계좌 아이디
    """
    bank_account_graphql_id: str
    bank_account: PlatformBankAccountDetail
    """입금 계좌 정보
    """
    currency: Currency
    """통화
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
    depositor_name: str
    """입금자명
    """
    is_for_test: bool
    """테스트 모드 여부
    """
    status_updated_at: str
    """상태 업데이트 일시
    (RFC 3339 date-time)
    """
    status: PlatformAccountTransferStatus
    """상태
    """
    deposit_memo: Optional[str] = field(default=None)
    """입금 계좌 적요
    """
    traded_at: Optional[str] = field(default=None)
    """이체 일시
    (RFC 3339 date-time)
    """


def _serialize_platform_deposit_account_transfer(obj: PlatformDepositAccountTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "DEPOSIT"
    entity["id"] = obj.id
    entity["bankAccountId"] = obj.bank_account_id
    entity["bankAccountGraphqlId"] = obj.bank_account_graphql_id
    entity["bankAccount"] = _serialize_platform_bank_account_detail(obj.bank_account)
    entity["currency"] = _serialize_currency(obj.currency)
    entity["amount"] = obj.amount
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    entity["depositorName"] = obj.depositor_name
    entity["isForTest"] = obj.is_for_test
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["status"] = _serialize_platform_account_transfer_status(obj.status)
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
    if obj.traded_at is not None:
        entity["tradedAt"] = obj.traded_at
    return entity


def _deserialize_platform_deposit_account_transfer(obj: Any) -> PlatformDepositAccountTransfer:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "DEPOSIT":
        raise ValueError("Expected 'DEPOSIT' for type")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "bankAccountId" not in obj:
        raise KeyError("Missing required field 'bankAccountId'")
    bank_account_id = obj["bankAccountId"]
    if not isinstance(bank_account_id, str):
        raise ValueError("Expected str for bank_account_id")
    if "bankAccountGraphqlId" not in obj:
        raise KeyError("Missing required field 'bankAccountGraphqlId'")
    bank_account_graphql_id = obj["bankAccountGraphqlId"]
    if not isinstance(bank_account_graphql_id, str):
        raise ValueError("Expected str for bank_account_graphql_id")
    if "bankAccount" not in obj:
        raise KeyError("Missing required field 'bankAccount'")
    bank_account = obj["bankAccount"]
    bank_account = _deserialize_platform_bank_account_detail(bank_account)
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError("Expected int for amount")
    if "createdAt" not in obj:
        raise KeyError("Missing required field 'createdAt'")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError("Expected str for created_at")
    if "updatedAt" not in obj:
        raise KeyError("Missing required field 'updatedAt'")
    updated_at = obj["updatedAt"]
    if not isinstance(updated_at, str):
        raise ValueError("Expected str for updated_at")
    if "depositorName" not in obj:
        raise KeyError("Missing required field 'depositorName'")
    depositor_name = obj["depositorName"]
    if not isinstance(depositor_name, str):
        raise ValueError("Expected str for depositor_name")
    if "isForTest" not in obj:
        raise KeyError("Missing required field 'isForTest'")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError("Expected bool for is_for_test")
    if "statusUpdatedAt" not in obj:
        raise KeyError("Missing required field 'statusUpdatedAt'")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError("Expected str for status_updated_at")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_platform_account_transfer_status(status)
    if "depositMemo" in obj:
        deposit_memo = obj["depositMemo"]
        if not isinstance(deposit_memo, str):
            raise ValueError("Expected str for deposit_memo")
    else:
        deposit_memo = None
    if "tradedAt" in obj:
        traded_at = obj["tradedAt"]
        if not isinstance(traded_at, str):
            raise ValueError("Expected str for traded_at")
    else:
        traded_at = None
    return PlatformDepositAccountTransfer(id, bank_account_id, bank_account_graphql_id, bank_account, currency, amount, created_at, updated_at, depositor_name, is_for_test, status_updated_at, status, deposit_memo, traded_at)
