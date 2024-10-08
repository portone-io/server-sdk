from __future__ import annotations
from typing import Any, Literal, Optional

PlatformAccountTransferType = Literal["DEPOSIT", "WITHDRAWAL_PARTNER_PAYOUT", "WITHDRAWAL_REMIT"]
"""계좌 이체 유형
"""


def _serialize_platform_account_transfer_type(obj: PlatformAccountTransferType) -> Any:
    return obj


def _deserialize_platform_account_transfer_type(obj: Any) -> PlatformAccountTransferType:
    if obj not in ["DEPOSIT", "WITHDRAWAL_PARTNER_PAYOUT", "WITHDRAWAL_REMIT"]:
        raise ValueError(f"{repr(obj)} is not PlatformAccountTransferType")
    return obj
