from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...platform.account_transfer.platform_account_transfer_status import PlatformAccountTransferStatus, _deserialize_platform_account_transfer_status, _serialize_platform_account_transfer_status

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
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "DEPOSIT":
        raise ValueError(f"{repr(type)} is not 'DEPOSIT'")
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
    if "depositorName" not in obj:
        raise KeyError(f"'depositorName' is not in {obj}")
    depositor_name = obj["depositorName"]
    if not isinstance(depositor_name, str):
        raise ValueError(f"{repr(depositor_name)} is not str")
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "statusUpdatedAt" not in obj:
        raise KeyError(f"'statusUpdatedAt' is not in {obj}")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError(f"{repr(status_updated_at)} is not str")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_account_transfer_status(status)
    if "depositMemo" in obj:
        deposit_memo = obj["depositMemo"]
        if not isinstance(deposit_memo, str):
            raise ValueError(f"{repr(deposit_memo)} is not str")
    else:
        deposit_memo = None
    if "tradedAt" in obj:
        traded_at = obj["tradedAt"]
        if not isinstance(traded_at, str):
            raise ValueError(f"{repr(traded_at)} is not str")
    else:
        traded_at = None
    return PlatformDepositAccountTransfer(id, bank_account_id, bank_account_graphql_id, currency, amount, created_at, updated_at, depositor_name, is_for_test, status_updated_at, status, deposit_memo, traded_at)
