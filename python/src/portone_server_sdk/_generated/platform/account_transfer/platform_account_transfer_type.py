from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformAccountTransferType = Union[Literal["DEPOSIT", "WITHDRAWAL_PARTNER_PAYOUT", "WITHDRAWAL_REMIT"], str]
"""계좌 이체 유형
"""


def _serialize_platform_account_transfer_type(obj: PlatformAccountTransferType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_account_transfer_type(obj: Any) -> PlatformAccountTransferType:
    return obj
