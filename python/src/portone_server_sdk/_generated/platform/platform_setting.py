from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSetting:
    """플랫폼 설정
    """
    default_withdrawal_memo: Optional[str] = field(default=None)
    """기본 보내는 이 통장 메모
    """
    default_deposit_memo: Optional[str] = field(default=None)
    """기본 받는 이 통장 메모
    """


def _serialize_platform_setting(obj: PlatformSetting) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.default_withdrawal_memo is not None:
        entity["defaultWithdrawalMemo"] = obj.default_withdrawal_memo
    if obj.default_deposit_memo is not None:
        entity["defaultDepositMemo"] = obj.default_deposit_memo
    return entity


def _deserialize_platform_setting(obj: Any) -> PlatformSetting:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "defaultWithdrawalMemo" in obj:
        default_withdrawal_memo = obj["defaultWithdrawalMemo"]
        if not isinstance(default_withdrawal_memo, str):
            raise ValueError(f"{repr(default_withdrawal_memo)} is not str")
    else:
        default_withdrawal_memo = None
    if "defaultDepositMemo" in obj:
        default_deposit_memo = obj["defaultDepositMemo"]
        if not isinstance(default_deposit_memo, str):
            raise ValueError(f"{repr(default_deposit_memo)} is not str")
    else:
        default_deposit_memo = None
    return PlatformSetting(default_withdrawal_memo, default_deposit_memo)
