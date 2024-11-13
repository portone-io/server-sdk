from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmIdentityVerificationBody:
    """본인인증 확인을 위한 입력 정보
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    otp: Optional[str] = field(default=None)
    """OTP (One-Time Password)

    SMS 방식에서만 사용됩니다.
    """


def _serialize_confirm_identity_verification_body(obj: ConfirmIdentityVerificationBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.otp is not None:
        entity["otp"] = obj.otp
    return entity


def _deserialize_confirm_identity_verification_body(obj: Any) -> ConfirmIdentityVerificationBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "otp" in obj:
        otp = obj["otp"]
        if not isinstance(otp, str):
            raise ValueError(f"{repr(otp)} is not str")
    else:
        otp = None
    return ConfirmIdentityVerificationBody(store_id, otp)
