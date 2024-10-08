from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.platform.account_transfer.platform_deposit_account_transfer import PlatformDepositAccountTransfer, _deserialize_platform_deposit_account_transfer, _serialize_platform_deposit_account_transfer
from portone_server_sdk._generated.platform.account_transfer.platform_partner_payout_account_transfer import PlatformPartnerPayoutAccountTransfer, _deserialize_platform_partner_payout_account_transfer, _serialize_platform_partner_payout_account_transfer
from portone_server_sdk._generated.platform.account_transfer.platform_remit_account_transfer import PlatformRemitAccountTransfer, _deserialize_platform_remit_account_transfer, _serialize_platform_remit_account_transfer

PlatformAccountTransfer = Union[PlatformDepositAccountTransfer, PlatformPartnerPayoutAccountTransfer, PlatformRemitAccountTransfer]
"""계좌 이체

송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
"""


def _serialize_platform_account_transfer(obj: PlatformAccountTransfer) -> Any:
    if obj.type == "DEPOSIT":
        return _serialize_platform_deposit_account_transfer(obj)
    if obj.type == "PARTNER_PAYOUT":
        return _serialize_platform_partner_payout_account_transfer(obj)
    if obj.type == "REMIT":
        return _serialize_platform_remit_account_transfer(obj)


def _deserialize_platform_account_transfer(obj: Any) -> PlatformAccountTransfer:
    try:
        return _deserialize_platform_deposit_account_transfer(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_payout_account_transfer(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_remit_account_transfer(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformAccountTransfer")
