from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..identity_verification.verified_identity_verification import VerifiedIdentityVerification, _deserialize_verified_identity_verification, _serialize_verified_identity_verification

@dataclass
class ConfirmIdentityVerificationResponse:
    """본인인증 확인 성공 응답
    """
    identity_verification: VerifiedIdentityVerification
    """완료된 본인인증 내역
    """


def _serialize_confirm_identity_verification_response(obj: ConfirmIdentityVerificationResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["identityVerification"] = _serialize_verified_identity_verification(obj.identity_verification)
    return entity


def _deserialize_confirm_identity_verification_response(obj: Any) -> ConfirmIdentityVerificationResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "identityVerification" not in obj:
        raise KeyError(f"'identityVerification' is not in {obj}")
    identity_verification = obj["identityVerification"]
    identity_verification = _deserialize_verified_identity_verification(identity_verification)
    return ConfirmIdentityVerificationResponse(identity_verification)
