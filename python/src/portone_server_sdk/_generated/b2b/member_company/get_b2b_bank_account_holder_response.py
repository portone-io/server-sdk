from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class GetB2bBankAccountHolderResponse:
    """예금주 조회 응답 정보
    """
    account_holder: str
    """예금주
    """


def _serialize_get_b2b_bank_account_holder_response(obj: GetB2bBankAccountHolderResponse) -> Any:
    entity = {}
    entity["accountHolder"] = obj.account_holder
    return entity


def _deserialize_get_b2b_bank_account_holder_response(obj: Any) -> GetB2bBankAccountHolderResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "accountHolder" not in obj:
        raise KeyError(f"'accountHolder' is not in {obj}")
    account_holder = obj["accountHolder"]
    if not isinstance(account_holder, str):
        raise ValueError(f"{repr(account_holder)} is not str")
    return GetB2bBankAccountHolderResponse(account_holder)
