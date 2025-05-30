from __future__ import annotations
from typing import Any, Optional, Union
from ...platform.account_transfer.platform_deposit_account_transfer import PlatformDepositAccountTransfer, _deserialize_platform_deposit_account_transfer, _serialize_platform_deposit_account_transfer
from ...platform.account_transfer.platform_withdrawal_account_transfer import PlatformWithdrawalAccountTransfer, _deserialize_platform_withdrawal_account_transfer, _serialize_platform_withdrawal_account_transfer

PlatformAccountTransfer = Union[PlatformDepositAccountTransfer, PlatformWithdrawalAccountTransfer, dict]
"""계좌 이체

송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
"""


def _serialize_platform_account_transfer(obj: PlatformAccountTransfer) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformDepositAccountTransfer):
        return _serialize_platform_deposit_account_transfer(obj)
    if isinstance(obj, PlatformWithdrawalAccountTransfer):
        return _serialize_platform_withdrawal_account_transfer(obj)


def _deserialize_platform_account_transfer(obj: Any) -> PlatformAccountTransfer:
    try:
        return _deserialize_platform_deposit_account_transfer(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_withdrawal_account_transfer(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformAccountTransfer")
