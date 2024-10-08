from __future__ import annotations
from typing import Any, Literal, Optional

IdentityVerificationOperator = Literal["SKT", "KT", "LGU", "SKT_MVNO", "KT_MVNO", "LGU_MVNO"]
"""본인인증 통신사
"""


def _serialize_identity_verification_operator(obj: IdentityVerificationOperator) -> Any:
    return obj


def _deserialize_identity_verification_operator(obj: Any) -> IdentityVerificationOperator:
    if obj not in ["SKT", "KT", "LGU", "SKT_MVNO", "KT_MVNO", "LGU_MVNO"]:
        raise ValueError(f"{repr(obj)} is not IdentityVerificationOperator")
    return obj
