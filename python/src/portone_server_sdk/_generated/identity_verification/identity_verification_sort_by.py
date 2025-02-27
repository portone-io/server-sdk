from __future__ import annotations
from typing import Any, Literal, Optional, Union

IdentityVerificationSortBy = Union[Literal["REQUESTED_AT", "VERIFIED_AT", "FAILED_AT", "STATUS_UPDATED_AT"], str]
"""본인인증 내역 정렬 기준
"""


def _serialize_identity_verification_sort_by(obj: IdentityVerificationSortBy) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_identity_verification_sort_by(obj: Any) -> IdentityVerificationSortBy:
    return obj
