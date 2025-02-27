from __future__ import annotations
from typing import Any, Literal, Optional, Union

IdentityVerificationStatus = Union[Literal["READY", "VERIFIED", "FAILED"], str]
"""본인인증 상태
"""


def _serialize_identity_verification_status(obj: IdentityVerificationStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_identity_verification_status(obj: Any) -> IdentityVerificationStatus:
    return obj
