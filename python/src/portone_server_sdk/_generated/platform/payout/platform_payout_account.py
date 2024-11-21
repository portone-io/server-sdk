from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.bank import Bank, _deserialize_bank, _serialize_bank

@dataclass
class PlatformPayoutAccount:
    bank: Bank
    number: str
    holder: str


def _serialize_platform_payout_account(obj: PlatformPayoutAccount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["bank"] = _serialize_bank(obj.bank)
    entity["number"] = obj.number
    entity["holder"] = obj.holder
    return entity


def _deserialize_platform_payout_account(obj: Any) -> PlatformPayoutAccount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "bank" not in obj:
        raise KeyError(f"'bank' is not in {obj}")
    bank = obj["bank"]
    bank = _deserialize_bank(bank)
    if "number" not in obj:
        raise KeyError(f"'number' is not in {obj}")
    number = obj["number"]
    if not isinstance(number, str):
        raise ValueError(f"{repr(number)} is not str")
    if "holder" not in obj:
        raise KeyError(f"'holder' is not in {obj}")
    holder = obj["holder"]
    if not isinstance(holder, str):
        raise ValueError(f"{repr(holder)} is not str")
    return PlatformPayoutAccount(bank, number, holder)
