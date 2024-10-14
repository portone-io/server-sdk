from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class PlatformDepositAccountTransfer:
    type: Literal["DEPOSIT"] = field(repr=False)
    """계좌 이체 유형
    """
    id: str
    """계좌 이체 아이디
    """
    currency: Currency
    """통화
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
    depositor_name: str
    """입금자명
    """
    deposit_memo: Optional[str]
    """입금 계좌 적요
    """


def _serialize_platform_deposit_account_transfer(obj: PlatformDepositAccountTransfer) -> Any:
    entity = {}
    entity["type"] = "DEPOSIT"
    entity["id"] = obj.id
    entity["currency"] = _serialize_currency(obj.currency)
    entity["amount"] = obj.amount
    entity["isForTest"] = obj.is_for_test
    entity["createdAt"] = obj.created_at
    entity["updatedAt"] = obj.updated_at
    entity["depositorName"] = obj.depositor_name
    if obj.deposit_memo is not None:
        entity["depositMemo"] = obj.deposit_memo
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
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
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
    if "depositorName" not in obj:
        raise KeyError(f"'depositorName' is not in {obj}")
    depositor_name = obj["depositorName"]
    if not isinstance(depositor_name, str):
        raise ValueError(f"{repr(depositor_name)} is not str")
    if "depositMemo" in obj:
        deposit_memo = obj["depositMemo"]
        if not isinstance(deposit_memo, str):
            raise ValueError(f"{repr(deposit_memo)} is not str")
    else:
        deposit_memo = None
    return PlatformDepositAccountTransfer(type, id, currency, amount, is_for_test, created_at, updated_at, depositor_name, deposit_memo)
