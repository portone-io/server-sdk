from __future__ import annotations
from typing import Any, Literal, Optional, Union

IdentityVerificationTimeRangeField = Union[Literal["REQUESTED_AT", "VERIFIED_AT", "FAILED_AT", "STATUS_UPDATED_AT"], str]
"""본인인증 다건 조회 시, 시각 범위를 적용할 필드
"""


def _serialize_identity_verification_time_range_field(obj: IdentityVerificationTimeRangeField) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_identity_verification_time_range_field(obj: Any) -> IdentityVerificationTimeRangeField:
    return obj
