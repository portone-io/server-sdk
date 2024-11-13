from __future__ import annotations
from typing import Any, Literal, Optional, Union

IdentityVerificationMethod = Union[Literal["SMS", "APP"], str]
"""본인인증 방식
"""


def _serialize_identity_verification_method(obj: IdentityVerificationMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_identity_verification_method(obj: Any) -> IdentityVerificationMethod:
    return obj
