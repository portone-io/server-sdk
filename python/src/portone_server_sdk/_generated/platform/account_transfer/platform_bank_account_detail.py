from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.bank import Bank, _deserialize_bank, _serialize_bank
from ...platform.account_transfer.platform_bank_account_provider import PlatformBankAccountProvider, _deserialize_platform_bank_account_provider, _serialize_platform_bank_account_provider

@dataclass
class PlatformBankAccountDetail:
    """계좌 상세 정보
    """
    account_number: str
    """계좌번호
    """
    bank: Bank
    """은행
    """
    provider: PlatformBankAccountProvider
    """제공자
    """
    holder: Optional[str] = field(default=None)
    """예금주명
    """


def _serialize_platform_bank_account_detail(obj: PlatformBankAccountDetail) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["accountNumber"] = obj.account_number
    entity["bank"] = _serialize_bank(obj.bank)
    entity["provider"] = _serialize_platform_bank_account_provider(obj.provider)
    if obj.holder is not None:
        entity["holder"] = obj.holder
    return entity


def _deserialize_platform_bank_account_detail(obj: Any) -> PlatformBankAccountDetail:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "accountNumber" not in obj:
        raise KeyError(f"'accountNumber' is not in {obj}")
    account_number = obj["accountNumber"]
    if not isinstance(account_number, str):
        raise ValueError(f"{repr(account_number)} is not str")
    if "bank" not in obj:
        raise KeyError(f"'bank' is not in {obj}")
    bank = obj["bank"]
    bank = _deserialize_bank(bank)
    if "provider" not in obj:
        raise KeyError(f"'provider' is not in {obj}")
    provider = obj["provider"]
    provider = _deserialize_platform_bank_account_provider(provider)
    if "holder" in obj:
        holder = obj["holder"]
        if not isinstance(holder, str):
            raise ValueError(f"{repr(holder)} is not str")
    else:
        holder = None
    return PlatformBankAccountDetail(account_number, bank, provider, holder)
