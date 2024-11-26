from __future__ import annotations
from typing import Any, Literal, Optional, Union

IdentityVerificationOperator = Union[Literal["SKT", "KT", "LGU", "SKT_MVNO", "KT_MVNO", "LGU_MVNO"], str]
"""본인인증 통신사
"""


def _serialize_identity_verification_operator(obj: IdentityVerificationOperator) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_identity_verification_operator(obj: Any) -> IdentityVerificationOperator:
    return obj
