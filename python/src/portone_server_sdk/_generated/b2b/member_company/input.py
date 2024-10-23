from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank

@dataclass
class Input:
    bank: Bank
    """은행
    """
    account_number: str
    """계좌번호
    """


def _serialize_input(obj: Input) -> Any:
    entity = {}
    entity["bank"] = _serialize_bank(obj.bank)
    entity["accountNumber"] = obj.account_number
    return entity


def _deserialize_input(obj: Any) -> Input:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "bank" not in obj:
        raise KeyError(f"'bank' is not in {obj}")
    bank = obj["bank"]
    bank = _deserialize_bank(bank)
    if "accountNumber" not in obj:
        raise KeyError(f"'accountNumber' is not in {obj}")
    account_number = obj["accountNumber"]
    if not isinstance(account_number, str):
        raise ValueError(f"{repr(account_number)} is not str")
    return Input(bank, account_number)
