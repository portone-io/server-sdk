from __future__ import annotations
from typing import Any, Optional, Union
from ..identity_verification.failed_identity_verification import FailedIdentityVerification, _deserialize_failed_identity_verification, _serialize_failed_identity_verification
from ..identity_verification.ready_identity_verification import ReadyIdentityVerification, _deserialize_ready_identity_verification, _serialize_ready_identity_verification
from ..identity_verification.verified_identity_verification import VerifiedIdentityVerification, _deserialize_verified_identity_verification, _serialize_verified_identity_verification

IdentityVerification = Union[FailedIdentityVerification, ReadyIdentityVerification, VerifiedIdentityVerification, dict]
"""본인인증 내역
"""


def _serialize_identity_verification(obj: IdentityVerification) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, FailedIdentityVerification):
        return _serialize_failed_identity_verification(obj)
    if isinstance(obj, ReadyIdentityVerification):
        return _serialize_ready_identity_verification(obj)
    if isinstance(obj, VerifiedIdentityVerification):
        return _serialize_verified_identity_verification(obj)


def _deserialize_identity_verification(obj: Any) -> IdentityVerification:
    try:
        return _deserialize_failed_identity_verification(obj)
    except Exception:
        pass
    try:
        return _deserialize_ready_identity_verification(obj)
    except Exception:
        pass
    try:
        return _deserialize_verified_identity_verification(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not IdentityVerification")
