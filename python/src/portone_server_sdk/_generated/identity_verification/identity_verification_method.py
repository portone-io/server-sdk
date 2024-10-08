from __future__ import annotations
from typing import Any, Literal, Optional

IdentityVerificationMethod = Literal["SMS", "APP"]
"""본인인증 방식
"""


def _serialize_identity_verification_method(obj: IdentityVerificationMethod) -> Any:
    return obj


def _deserialize_identity_verification_method(obj: Any) -> IdentityVerificationMethod:
    if obj not in ["SMS", "APP"]:
        raise ValueError(f"{repr(obj)} is not IdentityVerificationMethod")
    return obj
